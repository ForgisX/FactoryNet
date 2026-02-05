"""Paderborn Bearing Dataset Adapter.

Adapter for the Paderborn University bearing dataset (KAt-DataCenter),
featuring real and artificial bearing damages with run-to-failure data.

Dataset: https://mb.uni-paderborn.de/en/kat/research/bearing-datacenter/data-sets-and-download
Download: https://groups.uni-paderborn.de/kat/BearingDataCenter/
"""
from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import numpy as np

from .base_adapter import (
    BaseDatasetAdapter,
    DatasetMetadata,
    FaultType,
    RawEpisode,
    SensorChannel,
    SeverityLevel,
)
from .registry import register_adapter

logger = logging.getLogger(__name__)

# Paderborn dataset constants
PADERBORN_SAMPLING_RATE = 64000  # 64 kHz

# Bearing codes and their fault types
# K = healthy, KI = inner race, KA = outer race
PADERBORN_FAULT_CODES = {
    "K001": FaultType.NORMAL,
    "K002": FaultType.NORMAL,
    "K003": FaultType.NORMAL,
    "K004": FaultType.NORMAL,
    "K005": FaultType.NORMAL,
    "K006": FaultType.NORMAL,
    "KI01": FaultType.INNER_RACE,
    "KI03": FaultType.INNER_RACE,
    "KI04": FaultType.INNER_RACE,
    "KI05": FaultType.INNER_RACE,
    "KI07": FaultType.INNER_RACE,
    "KI08": FaultType.INNER_RACE,
    "KI14": FaultType.INNER_RACE,
    "KI16": FaultType.INNER_RACE,
    "KI17": FaultType.INNER_RACE,
    "KI18": FaultType.INNER_RACE,
    "KI21": FaultType.INNER_RACE,
    "KA01": FaultType.OUTER_RACE,
    "KA03": FaultType.OUTER_RACE,
    "KA04": FaultType.OUTER_RACE,
    "KA05": FaultType.OUTER_RACE,
    "KA06": FaultType.OUTER_RACE,
    "KA07": FaultType.OUTER_RACE,
    "KA08": FaultType.OUTER_RACE,
    "KA09": FaultType.OUTER_RACE,
    "KA15": FaultType.OUTER_RACE,
    "KA16": FaultType.OUTER_RACE,
    "KA22": FaultType.OUTER_RACE,
    "KA30": FaultType.OUTER_RACE,
}

# Damage types for severity mapping
# Artificial damages are generally more severe/controlled
DAMAGE_TYPE_SEVERITY = {
    "artificial": SeverityLevel.MODERATE,  # EDM, drilling, etc.
    "real": SeverityLevel.MINOR,  # Accelerated life test
    "fatigue": SeverityLevel.MODERATE,  # Fatigue testing
    "pitting": SeverityLevel.MINOR,
    "healthy": SeverityLevel.HEALTHY,
}

# Operating conditions in dataset
OPERATING_CONDITIONS = {
    "N09_M07_F10": {"rpm": 900, "load_nm": 0.7, "radial_force_n": 1000},
    "N15_M01_F10": {"rpm": 1500, "load_nm": 0.1, "radial_force_n": 1000},
    "N15_M07_F04": {"rpm": 1500, "load_nm": 0.7, "radial_force_n": 400},
    "N15_M07_F10": {"rpm": 1500, "load_nm": 0.7, "radial_force_n": 1000},
}


@register_adapter("paderborn_bearing", aliases=["paderborn", "kat"])
class PaderbornAdapter(BaseDatasetAdapter):
    """Adapter for Paderborn Bearing Dataset.

    The Paderborn dataset contains vibration measurements from a
    modular test rig with various bearing damage states:
    - Healthy bearings (K001-K006)
    - Inner race faults (KI*)
    - Outer race faults (KA*)

    Damage types include:
    - Artificial damage (EDM, drilling, electric engraving)
    - Real damage from accelerated life tests
    - Fatigue damage from repeated stress cycles

    Dataset characteristics:
    - Sampling rate: 64 kHz
    - Operating conditions: Variable speed and load
    - Sensors: Vibration, motor current, speed, temperature

    Example:
        adapter = PaderbornAdapter(data_dir="./data/paderborn")
        for episode in adapter.iter_episodes(limit=10):
            print(f"{episode.raw_id}: {episode.fault_type.value}")
    """

    METADATA = DatasetMetadata(
        name="paderborn_bearing",
        full_name="Paderborn University Bearing Dataset",
        description="KAt-DataCenter bearing fault dataset with real and artificial damages",
        source_url="https://groups.uni-paderborn.de/kat/BearingDataCenter/",
        citation=(
            "C. Lessmeier et al., 'Condition Monitoring of Bearing Damage in "
            "Electromechanical Drive Systems by Using Motor Current Signals of "
            "Electric Motors: A Benchmark Data Set for Data-Driven Classification,' "
            "PHM Europe, 2016."
        ),
        license="CC BY 4.0",
        num_samples=2156,  # Approximate
        file_format=".mat",
        sampling_rate_hz=64000,
        machine_type="bearing_test_rig",
        machine_synset="M.tst.bea.paderborn",
        download_size_mb=20000,  # ~20 GB
    )

    def __init__(
        self,
        data_dir: str | Path,
        cache_dir: Optional[str | Path] = None,
        segment_length: Optional[int] = None,
    ):
        """Initialize Paderborn adapter.

        Args:
            data_dir: Directory containing .mat files
            cache_dir: Optional cache directory
            segment_length: If set, segment signals into fixed-length episodes
        """
        super().__init__(data_dir, cache_dir)
        self.segment_length = segment_length

    @property
    def metadata(self) -> DatasetMetadata:
        """Return dataset metadata."""
        return self.METADATA

    def discover_files(self) -> List[Path]:
        """Discover all .mat files in the data directory."""
        files = list(self.data_dir.rglob("*.mat"))
        logger.info(f"Discovered {len(files)} .mat files in {self.data_dir}")
        return sorted(files)

    def parse_file(self, file_path: Path) -> Iterable[RawEpisode]:
        """Parse a Paderborn .mat file into RawEpisode(s).

        Args:
            file_path: Path to .mat file

        Yields:
            RawEpisode objects
        """
        try:
            from scipy.io import loadmat
        except ImportError:
            raise ImportError("scipy is required. Install with: pip install scipy")

        try:
            mat_data = loadmat(str(file_path), squeeze_me=True)
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {e}")
            return

        # Parse filename for metadata
        file_info = self._parse_filename(file_path)

        # Extract channels
        channels = self._extract_channels(mat_data, file_info)

        if not channels:
            logger.warning(f"No valid channels in {file_path}")
            return

        # Create episode
        yield self._create_episode(channels, file_info, file_path)

    def _parse_filename(self, file_path: Path) -> Dict[str, Any]:
        """Parse Paderborn filename for metadata.

        Filename format: {BearingCode}_{OperatingCondition}_{RunNumber}.mat
        Example: KA04_N15_M07_F10_1.mat

        Args:
            file_path: Path to file

        Returns:
            Dictionary with parsed metadata
        """
        filename = file_path.stem

        # Extract bearing code
        bearing_match = re.match(r"^(K[AI]?\d+)", filename)
        bearing_code = bearing_match.group(1) if bearing_match else "Unknown"

        # Extract operating condition
        op_match = re.search(r"(N\d+_M\d+_F\d+)", filename)
        op_condition = op_match.group(1) if op_match else None

        # Get operating parameters
        op_params = OPERATING_CONDITIONS.get(op_condition, {
            "rpm": 1500, "load_nm": 0.7, "radial_force_n": 1000
        })

        # Determine fault type
        fault_type = PADERBORN_FAULT_CODES.get(bearing_code, FaultType.UNKNOWN)

        # Determine severity based on bearing code prefix
        if bearing_code.startswith("K0"):
            severity = SeverityLevel.HEALTHY
        elif "artificial" in file_path.parts or bearing_code in ["KI01", "KI03", "KA01", "KA03"]:
            severity = SeverityLevel.MODERATE
        else:
            severity = SeverityLevel.MINOR

        return {
            "bearing_code": bearing_code,
            "op_condition": op_condition,
            "fault_type": fault_type,
            "severity": severity,
            "rpm": op_params.get("rpm", 1500),
            "load_nm": op_params.get("load_nm", 0.7),
            "radial_force_n": op_params.get("radial_force_n", 1000),
        }

    def _extract_channels(
        self,
        mat_data: Dict[str, Any],
        file_info: Dict[str, Any],
    ) -> List[SensorChannel]:
        """Extract sensor channels from .mat file.

        Paderborn files typically contain:
        - vibration: Accelerometer data
        - current_1, current_2: Motor phase currents
        - speed: Rotational speed
        - temp_2: Temperature

        Args:
            mat_data: Loaded .mat data
            file_info: Parsed file metadata

        Returns:
            List of SensorChannel objects
        """
        channels = []

        # Channel name mapping
        channel_map = {
            "vibration": ("vibration", "g"),
            "current_1": ("motor_current_1", "A"),
            "current_2": ("motor_current_2", "A"),
            "speed": ("speed", "rpm"),
            "temp_2": ("temperature", "°C"),
        }

        for mat_key, (channel_type, unit) in channel_map.items():
            if mat_key in mat_data:
                data = mat_data[mat_key]
                if isinstance(data, np.ndarray):
                    data = data.flatten().astype(np.float64)
                    if len(data) > 100:
                        channels.append(SensorChannel(
                            channel_id=f"{file_info['bearing_code']}_{mat_key}",
                            channel_type=channel_type,
                            unit=unit,
                            data=data.tolist(),
                            sampling_rate_hz=PADERBORN_SAMPLING_RATE,
                        ))

        # Try alternate structure (nested in struct)
        if not channels:
            for key in mat_data.keys():
                if key.startswith("__"):
                    continue
                data = mat_data[key]
                if isinstance(data, np.ndarray) and data.ndim == 1 and len(data) > 1000:
                    channels.append(SensorChannel(
                        channel_id=f"{file_info['bearing_code']}_{key}",
                        channel_type="vibration",
                        unit="g",
                        data=data.astype(np.float64).tolist(),
                        sampling_rate_hz=PADERBORN_SAMPLING_RATE,
                    ))
                    break

        return channels

    def _create_episode(
        self,
        channels: List[SensorChannel],
        file_info: Dict[str, Any],
        file_path: Path,
    ) -> RawEpisode:
        """Create RawEpisode from channels and metadata."""
        # Determine fault location
        fault_location = None
        if file_info["fault_type"] == FaultType.INNER_RACE:
            fault_location = "inner_race"
        elif file_info["fault_type"] == FaultType.OUTER_RACE:
            fault_location = "outer_race"

        return RawEpisode(
            raw_id=f"paderborn_{file_path.stem}",
            source_dataset="paderborn_bearing",
            source_file=file_path.name,
            channels=channels,
            fault_type=file_info["fault_type"],
            fault_location=fault_location,
            severity=file_info["severity"],
            rpm=file_info["rpm"],
            raw_metadata={
                "bearing_code": file_info["bearing_code"],
                "operating_condition": file_info["op_condition"],
                "load_nm": file_info["load_nm"],
                "radial_force_n": file_info["radial_force_n"],
                "sampling_rate_hz": PADERBORN_SAMPLING_RATE,
            },
        )
