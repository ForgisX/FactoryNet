import logging
from pathlib import Path
from typing import List, Optional

from docling.document_converter import DocumentConverter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ManualIngestor:
    def __init__(self, input_dir: Path, output_dir: Path):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.converter = DocumentConverter()

    def process_all(self):
        """Process all PDFs in the input directory."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        pdf_files = list(self.input_dir.glob("*.pdf"))
        if not pdf_files:
            logger.warning(f"No PDF files found in {self.input_dir}")
            return

        for pdf_path in pdf_files:
            self.process_single(pdf_path)

    def process_single(self, pdf_path: Path) -> Optional[Path]:
        """Process a single PDF file and return the path to the generated Markdown file."""
        try:
            logger.info(f"Converting: {pdf_path.name}")
            
            # Run Docling
            result = self.converter.convert(str(pdf_path))
            doc = result.document
            
            # Export to markdown
            markdown = doc.export_to_markdown()
            
            # Save to file
            out_path = self.output_dir / f"{pdf_path.stem}.md"
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(markdown)
            
            logger.info(f"  -> Saved markdown to {out_path}")
            return out_path
            
        except Exception as e:
            logger.error(f"Failed to convert {pdf_path.name}: {e}")
            return None

if __name__ == "__main__":
    # Default paths for standalone execution
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    MANUALS_DIR = PROJECT_ROOT / "manual-extraction-pipeline" / "sample_manuals"
    OUTPUT_DIR = PROJECT_ROOT / "data" / "docling_outputs"
    
    ingestor = ManualIngestor(MANUALS_DIR, OUTPUT_DIR)
    ingestor.process_all()
