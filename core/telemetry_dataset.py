from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, Optional

import numpy as np
from datasets import Dataset, Features, Sequence as HFSequence, Value
from tqdm.auto import tqdm


@dataclass
class TelemetryData:
    """Single univariate telemetry time series with attached information.

    This is the central struct produced by the telemetry_data_generator and
    consumed when building a Hugging Face Dataset.
    """

    id: str
    time: np.ndarray
    timeseries: np.ndarray
    metadata: Dict[str, Any]
    statistics: Dict[str, float]

    def __post_init__(self) -> None:
        # Ensure numpy array types/shapes are consistent and compact.
        # Use float32 to halve memory compared to float64.
        self.time = np.asarray(self.time, dtype=np.float32)
        self.timeseries = np.asarray(self.timeseries, dtype=np.float32)

        if self.time.ndim != 1:
            raise ValueError("time must be a 1D array")
        if self.timeseries.ndim != 1:
            raise ValueError("timeseries must be a 1D array")
        if self.time.shape[0] != self.timeseries.shape[0]:
            raise ValueError("time and timeseries must have the same length")

    def to_hf_row(self) -> Dict[str, Any]:
        """Convert to a row suitable for Hugging Face Datasets."""

        domain = self.metadata.get("domain", "")
        subtype = self.metadata.get("subtype", "")

        stats = {
            "mean": float(self.statistics.get("mean", float(np.mean(self.timeseries)))),
            "std": float(self.statistics.get("std", float(np.std(self.timeseries)))),
            "min": float(self.statistics.get("min", float(np.min(self.timeseries)))),
            "max": float(self.statistics.get("max", float(np.max(self.timeseries)))),
        }

        return {
            "id": self.id,
            "timestamps": self.time,
            "values": self.timeseries,
            "domain": domain,
            "subtype": subtype,
            "statistics": stats,
        }


def telemetry_features() -> Features:
    """HF Features definition for TelemetryData rows."""

    return Features(
        {
            "id": Value("string"),
            "timestamps": HFSequence(Value("float32")),
            "values": HFSequence(Value("float32")),
            "domain": Value("string"),
            "subtype": Value("string"),
            "statistics": {
                "mean": Value("float32"),
                "std": Value("float32"),
                "min": Value("float32"),
                "max": Value("float32"),
            },
        }
    )


def build_telemetry_dataset(
    records: Iterable[TelemetryData],
    total: Optional[int] = None,
) -> Dataset:
    """Create a Hugging Face Dataset from TelemetryData objects.

    Accepts any iterable, including generators such as `iter_telemetry`.
    For generators, this avoids keeping a separate in‑memory list of
    `TelemetryData` objects while still building a single in‑memory
    Dataset (required by `datasets.Dataset`).
    """

    if total is None:
        try:
            total = len(records)  # type: ignore[arg-type]
        except TypeError:
            # records is a generator/iterator without a known length
            total = None

    rows = [
        record.to_hf_row()
        for record in tqdm(
            records,
            total=total,
            desc="Converting telemetry to HF rows",
            unit="series",
        )
    ]

    return Dataset.from_list(rows, features=telemetry_features())


if __name__ == "__main__":
    from telemetry_data_generator import TimeseriesGenerator
    from telemetry_dataset import build_telemetry_dataset

    gen = TimeseriesGenerator(
            n_timeseries=1,        # placeholder; generate_telemetry overrides this
            time_duration=10.0,    # seconds
            frequency=100.0,       # Hz
            seed=42,
        )
    

    total = 500000
    telemetry_iter = gen.iter_telemetry(
        total=total,
        type_proportions={
            "industrial": 20,
            "step": 20,
            "sine": 20,
            "random_walk": 20,
            "stock": 20,
        },
    )

    ds = build_telemetry_dataset(telemetry_iter, total=total)
    
    ds.save_to_disk(dataset_path='/home/gpiatelli/Xelerit/FactorySet/dataset')
