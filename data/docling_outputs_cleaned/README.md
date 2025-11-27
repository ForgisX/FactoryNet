# Cleaned Docling Outputs

This directory contains cleaned versions of markdown files extracted from PDFs using Docling.

## Cleaning Process

The original docling-extracted markdown files contained many meaningless character sequences that were artifacts from PDF parsing, such as:
- Repeated `/G` sequences (e.g., `/G2/G3/G4/G5/G3/G6/G4/G7/G8/G8/G8/G8...`)
- Table rows filled with these meaningless patterns
- Other similar parsing artifacts

## Cleaning Script

The cleaning was performed using `scripts/clean_docling_output.py`, which:
1. Identifies lines with more than 10 `/G` sequences
2. Removes lines where >70% of content is `/G` patterns
3. Removes table rows where >50% of cells contain meaningless sequences
4. Preserves all meaningful content including headings, paragraphs, and proper tables

## Results

### File: B-70254EN_01_101028_fanuc_laser_digital.md
- **Original**: 4,855 lines, 311,852 bytes
- **Cleaned**: 4,740 lines, 185,547 bytes
- **Removed**: 115 lines (2.4%)
- **Size reduction**: ~40%

## Usage

The cleaned markdown files are ready for further processing, such as:
- Indexing for RAG (Retrieval-Augmented Generation)
- Text analysis
- Information extraction
- Manual review

All meaningful content has been preserved while removing PDF parsing artifacts that would interfere with downstream processing.
