"""
Script 1: Ingest PDF manuals and convert to clean markdown.

Usage:
    python 1_ingest_to_markdown.py <input_pdf_path> [output_dir]
    
Example:
    python 1_ingest_to_markdown.py sample_manuals/manual.pdf data/markdown_outputs
"""

import sys
import re
import logging
from pathlib import Path
from docling.document_converter import DocumentConverter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def clean_markdown(content: str) -> str:
    """
    Remove meaningless character sequences from docling output.
    
    Args:
        content: Raw markdown content from docling
        
    Returns:
        Cleaned markdown content
    """
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines (keep them)
        if not stripped:
            cleaned_lines.append(line)
            continue
        
        # Check for lines with excessive /G sequences (PDF parsing artifacts)
        g_matches = re.findall(r'/G\d+', stripped)
        
        # Skip lines with more than 10 /G sequences
        if len(g_matches) > 10:
            continue
        
        # Skip lines where >70% is /G sequences
        if g_matches:
            g_content_length = sum(len(match) for match in g_matches)
            total_length = len(stripped.replace(' ', ''))
            if total_length > 0 and (g_content_length / total_length) > 0.7:
                continue
        
        # Skip table rows filled with meaningless sequences
        if '|' in line:
            cells = line.split('|')
            meaningless_cells = sum(1 for cell in cells if len(re.findall(r'/G\d+', cell.strip())) > 3)
            total_cells = sum(1 for cell in cells if cell.strip())
            if total_cells > 0 and (meaningless_cells / total_cells) > 0.5:
                continue
        
        # Keep the line
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)


def ingest_pdf_to_markdown(pdf_path: Path, output_dir: Path) -> Path:
    """
    Convert a PDF manual to clean markdown.
    
    Args:
        pdf_path: Path to input PDF file
        output_dir: Directory to save markdown output
        
    Returns:
        Path to the generated markdown file
    """
    logger.info(f"Processing: {pdf_path.name}")
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize docling converter
    logger.info("Initializing docling converter...")
    converter = DocumentConverter()
    
    # Convert PDF to markdown
    logger.info("Converting PDF (this may take a few minutes)...")
    result = converter.convert(str(pdf_path))
    doc = result.document
    
    # Export to markdown
    logger.info("Exporting to markdown...")
    raw_markdown = doc.export_to_markdown()
    
    # Clean the markdown
    logger.info("Cleaning markdown (removing PDF artifacts)...")
    clean_md = clean_markdown(raw_markdown)
    
    # Save to file
    output_path = output_dir / f"{pdf_path.stem}.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(clean_md)
    
    # Report statistics
    original_lines = len(raw_markdown.split('\n'))
    cleaned_lines = len(clean_md.split('\n'))
    removed_lines = original_lines - cleaned_lines
    
    logger.info(f"✓ Saved: {output_path}")
    logger.info(f"  Original: {original_lines} lines, {len(raw_markdown)} bytes")
    logger.info(f"  Cleaned: {cleaned_lines} lines, {len(clean_md)} bytes")
    logger.info(f"  Removed: {removed_lines} lines ({removed_lines/original_lines*100:.1f}%)")
    
    return output_path


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    # Parse arguments
    pdf_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("data/markdown_outputs")
    
    # Validate input
    if not pdf_path.exists():
        logger.error(f"PDF file not found: {pdf_path}")
        sys.exit(1)
    
    if not pdf_path.suffix.lower() == '.pdf':
        logger.error(f"Input file must be a PDF: {pdf_path}")
        sys.exit(1)
    
    # Process
    try:
        output_path = ingest_pdf_to_markdown(pdf_path, output_dir)
        logger.info(f"\n✓ SUCCESS: Markdown saved to {output_path}")
    except Exception as e:
        logger.error(f"\n✗ FAILED: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
