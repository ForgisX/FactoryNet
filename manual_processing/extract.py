import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FaultExtractor:
    def __init__(self):
        pass

    def extract(self, markdown_path: Path) -> List[Dict]:
        """
        Extract fault codes and instructions from a markdown file.
        Returns a list of dictionaries, each representing a fault.
        """
        logger.info(f"Extracting faults from: {markdown_path.name}")
        
        try:
            with open(markdown_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Level 1: Structural/Regex Extraction
            # This is a placeholder for heuristic extraction.
            # We look for patterns like "Error Code: X" or tables with "Fault" headers.
            
            faults = self._extract_heuristic(content)
            
            if not faults:
                logger.info("No faults found with heuristics. Level 2 (Semantic) needed.")
                # Level 2: Semantic Extraction (LlamaIndex) would go here
                # faults = self._extract_semantic(content)
            
            return faults

        except Exception as e:
            logger.error(f"Failed to extract from {markdown_path.name}: {e}")
            return []

    def _extract_heuristic(self, content: str) -> List[Dict]:
        """
        Attempt to extract faults using regex and structure.
        """
        faults = []
        
        # Example heuristic: Look for lines starting with "Error Code" or "Fault"
        # This is very basic and needs to be tuned based on actual manual content.
        
        # Regex for "Error Code <number>: <description>"
        # Adjust regex based on the actual format in the manuals
        pattern = re.compile(r"(?:Error Code|Fault Code)\s*[:\-\.]?\s*(\w+)\s*[:\-\.]?\s*(.+)", re.IGNORECASE)
        
        for line in content.split('\n'):
            match = pattern.search(line)
            if match:
                code = match.group(1)
                description = match.group(2)
                faults.append({
                    "code": code,
                    "description": description.strip(),
                    "source": "heuristic"
                })
        
        return faults

    def _extract_semantic(self, content: str) -> List[Dict]:
        """
        Placeholder for LlamaIndex based extraction.
        """
        # TODO: Implement LlamaIndex extraction
        return []

if __name__ == "__main__":
    # Test with a sample file if it exists
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    SAMPLE_MD = PROJECT_ROOT / "data" / "docling_outputs" / "cnc_milling_manual_students_digital.md"
    
    if SAMPLE_MD.exists():
        extractor = FaultExtractor()
        results = extractor.extract(SAMPLE_MD)
        print(json.dumps(results, indent=2))
    else:
        print(f"Sample file {SAMPLE_MD} not found. Run ingest.py first.")
