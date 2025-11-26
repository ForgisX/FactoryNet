import os
from pathlib import Path

from docling.document_converter import DocumentConverter


# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MANUALS_DIR = PROJECT_ROOT / "data" / "manuals"
OUTPUT_DIR = PROJECT_ROOT / "data" / "docling_outputs"

def convert_manuals():
    # Ensure output dir exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Init Docling converter with default pipeline
    converter = DocumentConverter()

    # Iterate over all PDFs in data/manuals
    for pdf_path in MANUALS_DIR.glob("*.pdf"):
        print(f"Converting: {pdf_path.name}")

        # Run Docling
        result = converter.convert(str(pdf_path))

        # Get DoclingDocument
        doc = result.document

        # Export to markdown (great input format for GPT later)
        markdown = doc.export_to_markdown()

        # Build output path with same base name, .md extension
        out_path = OUTPUT_DIR / f"{pdf_path.stem}.md"

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"  → Saved markdown to {out_path}")

if __name__ == "__main__":
    convert_manuals()
