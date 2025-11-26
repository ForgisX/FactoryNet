import logging
from pathlib import Path
import json

from manual_processing.ingest import ManualIngestor
from manual_processing.extract import FaultExtractor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline():
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    MANUALS_DIR = PROJECT_ROOT / "manual_processing" / "sample_manuals"
    OUTPUT_DIR = PROJECT_ROOT / "data" / "docling_outputs"
    RESULTS_DIR = PROJECT_ROOT / "data" / "extracted_faults"
    
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Ingestion
    logger.info("Starting Ingestion Phase...")
    ingestor = ManualIngestor(MANUALS_DIR, OUTPUT_DIR)
    ingestor.process_all()
    
    # 2. Extraction
    logger.info("Starting Extraction Phase...")
    extractor = FaultExtractor()
    
    for md_file in OUTPUT_DIR.glob("*.md"):
        faults = extractor.extract(md_file)
        
        if faults:
            output_file = RESULTS_DIR / f"{md_file.stem}_faults.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(faults, f, indent=2)
            logger.info(f"Saved {len(faults)} faults to {output_file}")
        else:
            logger.warning(f"No faults extracted from {md_file.name}")

if __name__ == "__main__":
    run_pipeline()
