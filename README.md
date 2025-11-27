# FactorySet

A toolkit for processing factory equipment manuals into structured data for fault diagnosis and maintenance.

## Quick Start

### Installation

```bash
# Clone and setup
git clone <repository-url>
cd FactorySet

# Create virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt
```

### Process a Manual

```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Process a PDF manual (full pipeline)
python manual_processing/3_run_pipeline.py manual_processing/sample_manuals/manual.pdf data/output

# Or run individual steps
python manual_processing/1_ingest_to_markdown.py manual.pdf data/markdown
python manual_processing/2_extract_faults.py data/markdown/manual.md data/extracted/manual.json
```

## Manual Processing Pipeline

Three simple scripts for converting PDF manuals to structured data:

1. **`1_ingest_to_markdown.py`** - PDF → Clean Markdown
   - Extracts text, tables, and structure using Docling
   - Removes PDF parsing artifacts automatically

2. **`2_extract_faults.py`** - Markdown → Structured JSON
   - Extracts fault codes with descriptions and fixes
   - Extracts machine metadata (model, manufacturer, manual ID)
   - Extracts maintenance procedures

3. **`3_run_pipeline.py`** - Pipeline Orchestrator
   - Runs complete pipeline on single PDFs or directories
   - Handles errors and provides detailed logging

### Example Output

```json
{
  "metadata": {
    "model": "C1000 i A",
    "manufacturer": "FANUC",
    "manual_id": "B-70254EN/01",
    "manual_type": "Operator's Manual"
  },
  "fault_codes": [
    {
      "code": "4085",
      "description": "MIRROR CLEANING",
      "fixing_instruction": "Clean or replace mirror",
      "extraction_method": "table_extraction"
    }
  ],
  "maintenance_procedures": [...]
}
```

## Project Structure

```
FactorySet/
├── manual_processing/          # Manual processing scripts
│   ├── 1_ingest_to_markdown.py    # PDF → Markdown
│   ├── 2_extract_faults.py        # Markdown → JSON
│   ├── 3_run_pipeline.py          # Pipeline orchestrator
│   └── sample_manuals/            # Test PDFs
├── data/                       # Processed data outputs
│   ├── markdown/                  # Cleaned markdown files
│   └── extracted/                 # Structured JSON data
├── core/                       # Core utilities (future)
└── docs/                       # Documentation
```

## Dataset Structure

The extracted data contains:

- **Fault Codes**: Error codes with descriptions and fixing instructions
- **Metadata**: Machine model, manufacturer, manual ID, manual type
- **Maintenance**: Periodic maintenance schedules and procedures
- **Statistics**: Extraction quality metrics

## Development

### Code Style

This repository uses pre-commit hooks with Black, isort, and flake8:

```bash
# Install pre-commit hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

### Documentation

View documentation locally:

```bash
mkdocs serve
# Open http://127.0.0.1:8000
```

## Requirements

- Python 3.8+
- docling (for PDF extraction)
- pypdf (for fast text extraction)

See `requirements.txt` for full list.

## License

Part of the Xelerit project suite.