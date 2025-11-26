import logging
from pathlib import Path
import json
import sys

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))

from manual_processing.ingest import ManualIngestor
from manual_processing.extract import FaultExtractor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_single_manual():
    PROJECT_ROOT = Path(__file__).resolve().parent
    MANUAL_PATH = PROJECT_ROOT / "manual_processing" / "sample_manuals" / "B-70254EN_01_101028_fanuc_laser_digital.pdf"
    OUTPUT_DIR = PROJECT_ROOT / "data" / "docling_outputs"
    RESULTS_DIR = PROJECT_ROOT / "data" / "extracted_faults"
    
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    if not MANUAL_PATH.exists():
        logger.error(f"Manual not found at {MANUAL_PATH}")
        return

    # 1. Ingestion
    logger.info(f"Starting Ingestion for {MANUAL_PATH.name}...")
    ingestor = ManualIngestor(MANUAL_PATH.parent, OUTPUT_DIR)
    # We use process_single directly
    md_path = ingestor.process_single(MANUAL_PATH)
    
    if not md_path:
        logger.error("Ingestion failed.")
        return

    # 2. Extraction
    logger.info(f"Starting Extraction for {md_path.name}...")
    extractor = FaultExtractor()
    faults = extractor.extract(md_path)
    
    if faults:
        output_file = RESULTS_DIR / f"{md_path.stem}_faults.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(faults, f, indent=2)
        logger.info(f"Saved {len(faults)} faults to {output_file}")
        print(json.dumps(faults, indent=2)) # Print to stdout for user to see
    else:
        logger.warning(f"No faults extracted from {md_path.name}")

if __name__ == "__main__":
    test_single_manual()
