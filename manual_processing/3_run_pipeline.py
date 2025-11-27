"""
Script 3: Pipeline orchestrator - runs the complete manual processing pipeline.

This script orchestrates the entire pipeline:
1. Ingest PDF → Clean Markdown
2. Extract Faults & Metadata → JSON

Usage:
    python 3_run_pipeline.py <pdf_path> [output_base_dir]
    python 3_run_pipeline.py <pdf_directory> [output_base_dir]  # Process all PDFs in directory
    
Examples:
    # Process single PDF
    python 3_run_pipeline.py sample_manuals/manual.pdf data/pipeline_output
    
    # Process all PDFs in a directory
    python 3_run_pipeline.py sample_manuals/ data/pipeline_output
"""

import sys
import logging
from pathlib import Path
from typing import List
import subprocess

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_pipeline_for_pdf(pdf_path: Path, output_base_dir: Path) -> bool:
    """
    Run the complete pipeline for a single PDF.
    
    Args:
        pdf_path: Path to PDF file
        output_base_dir: Base directory for all outputs
        
    Returns:
        True if successful, False otherwise
    """
    logger.info(f"\n{'='*80}")
    logger.info(f"PROCESSING: {pdf_path.name}")
    logger.info(f"{'='*80}\n")
    
    # Define output paths
    markdown_dir = output_base_dir / "markdown"
    extracted_dir = output_base_dir / "extracted"
    
    markdown_path = markdown_dir / f"{pdf_path.stem}.md"
    json_path = extracted_dir / f"{pdf_path.stem}_extracted.json"
    
    try:
        # Step 1: Ingest PDF to Markdown
        logger.info("STEP 1/2: Converting PDF to clean markdown...")
        logger.info("-" * 80)
        
        result = subprocess.run(
            [
                sys.executable,
                "1_ingest_to_markdown.py",
                str(pdf_path.absolute()),
                str(markdown_dir.absolute())
            ],
            cwd=Path(__file__).parent,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            logger.error(f"Step 1 failed: {result.stderr}")
            return False
        
        logger.info(result.stdout)
        
        # Verify markdown was created
        if not markdown_path.exists():
            logger.error(f"Markdown file not created: {markdown_path}")
            return False
        
        # Step 2: Extract Faults and Metadata
        logger.info("\nSTEP 2/2: Extracting faults and metadata...")
        logger.info("-" * 80)
        
        result = subprocess.run(
            [
                sys.executable,
                "2_extract_faults.py",
                str(markdown_path.absolute()),
                str(json_path.absolute())
            ],
            cwd=Path(__file__).parent,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            logger.error(f"Step 2 failed: {result.stderr}")
            return False
        
        logger.info(result.stdout)
        
        # Verify JSON was created
        if not json_path.exists():
            logger.error(f"Extracted JSON not created: {json_path}")
            return False
        
        # Success summary
        logger.info(f"\n{'='*80}")
        logger.info(f"✓ PIPELINE COMPLETE: {pdf_path.name}")
        logger.info(f"{'='*80}")
        logger.info(f"  Markdown: {markdown_path}")
        logger.info(f"  Extracted: {json_path}")
        
        return True
        
    except Exception as e:
        logger.error(f"Pipeline failed for {pdf_path.name}: {e}", exc_info=True)
        return False


def find_pdfs(path: Path) -> List[Path]:
    """
    Find all PDF files in a path (file or directory).
    
    Args:
        path: Path to PDF file or directory
        
    Returns:
        List of PDF paths
    """
    if path.is_file():
        if path.suffix.lower() == '.pdf':
            return [path]
        else:
            logger.error(f"File is not a PDF: {path}")
            return []
    elif path.is_dir():
        pdfs = list(path.glob("*.pdf"))
        if not pdfs:
            logger.warning(f"No PDF files found in directory: {path}")
        return pdfs
    else:
        logger.error(f"Path does not exist: {path}")
        return []


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    # Parse arguments
    input_path = Path(sys.argv[1])
    output_base_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("data/pipeline_output")
    
    # Validate input
    if not input_path.exists():
        logger.error(f"Input path not found: {input_path}")
        sys.exit(1)
    
    # Find PDFs to process
    pdf_files = find_pdfs(input_path)
    
    if not pdf_files:
        logger.error("No PDF files to process")
        sys.exit(1)
    
    # Process each PDF
    logger.info(f"\n{'='*80}")
    logger.info(f"MANUAL PROCESSING PIPELINE")
    logger.info(f"{'='*80}")
    logger.info(f"Input: {input_path}")
    logger.info(f"Output: {output_base_dir}")
    logger.info(f"PDFs to process: {len(pdf_files)}")
    logger.info(f"{'='*80}\n")
    
    results = []
    for pdf_path in pdf_files:
        success = run_pipeline_for_pdf(pdf_path, output_base_dir)
        results.append((pdf_path.name, success))
    
    # Final summary
    logger.info(f"\n\n{'='*80}")
    logger.info(f"PIPELINE SUMMARY")
    logger.info(f"{'='*80}")
    
    successful = sum(1 for _, success in results if success)
    failed = len(results) - successful
    
    logger.info(f"Total PDFs: {len(results)}")
    logger.info(f"Successful: {successful}")
    logger.info(f"Failed: {failed}")
    
    if failed > 0:
        logger.info(f"\nFailed files:")
        for name, success in results:
            if not success:
                logger.info(f"  ✗ {name}")
    
    logger.info(f"\nOutput directory: {output_base_dir}")
    logger.info(f"  Markdown files: {output_base_dir / 'markdown'}")
    logger.info(f"  Extracted data: {output_base_dir / 'extracted'}")
    logger.info(f"{'='*80}\n")
    
    # Exit with error code if any failed
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
