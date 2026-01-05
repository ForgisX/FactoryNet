# Manual Processing Package

Simple, robust POC for processing factory equipment manuals (PDFs) into structured data.

## Overview

This package contains **3 simple scripts** that form a complete pipeline:

1. **`1_ingest_to_markdown.py`** - Convert PDF to clean markdown
2. **`2_extract_faults.py`** - Extract fault codes, fixes, and metadata
3. **`3_run_pipeline.py`** - Orchestrate the complete pipeline

## Quick Start

### Process a single manual

```bash
# Run the complete pipeline on one PDF
python 3_run_pipeline.py sample_manuals/manual.pdf data/output

# Or run steps individually:
python 1_ingest_to_markdown.py sample_manuals/manual.pdf data/markdown
python 2_extract_faults.py data/markdown/manual.md data/extracted/manual.json
```

### Process multiple manuals

```bash
# Process all PDFs in a directory
python 3_run_pipeline.py sample_manuals/ data/output
```

## Script Details

### 1. Ingest to Markdown (`1_ingest_to_markdown.py`)

**Purpose**: Convert PDF manuals to clean, readable markdown.

**What it does**:
- Uses Docling to extract text, tables, and structure from PDFs
- Automatically cleans up PDF parsing artifacts (e.g., `/G2/G3/G4...` sequences)
- Outputs clean markdown ready for further processing

**Usage**:
```bash
python 1_ingest_to_markdown.py <pdf_path> [output_dir]
```

**Example**:
```bash
python 1_ingest_to_markdown.py sample_manuals/fanuc_laser.pdf data/markdown
```

**Output**: Clean markdown file in `output_dir/`

---

### 2. Extract Faults (`2_extract_faults.py`)

**Purpose**: Extract structured information from markdown manuals.

**What it extracts**:
- **Fault codes** with descriptions and fixing instructions
- **Machine metadata** (model, manufacturer, manual ID)
- **Maintenance procedures** and schedules

**Extraction methods**:
- Regex pattern matching for fault codes
- Table parsing for structured data
- Heuristic text analysis for metadata

**Usage**:
```bash
python 2_extract_faults.py <markdown_path> [output_json_path]
```

**Example**:
```bash
python 2_extract_faults.py data/markdown/fanuc_laser.md data/extracted/fanuc_laser.json
```

**Output**: JSON file with structured data:
```json
{
  "source_file": "fanuc_laser.md",
  "metadata": {
    "model": "C1000 i A",
    "manufacturer": "FANUC",
    "manual_id": "B-70254EN/01",
    "manual_type": "Operator's Manual"
  },
  "fault_codes": [
    {
      "code": "4085",
      "description": "Laser output decreased",
      "fixing_instruction": "Clean or replace mirror",
      "extraction_method": "pattern_match"
    }
  ],
  "maintenance_procedures": [...],
  "extraction_stats": {...}
}
```

---

### 3. Run Pipeline (`3_run_pipeline.py`)

**Purpose**: Orchestrate the complete processing pipeline.

**What it does**:
- Runs both scripts in sequence
- Handles single PDFs or entire directories
- Provides progress logging and error handling
- Generates summary report

**Usage**:
```bash
python 3_run_pipeline.py <pdf_path_or_directory> [output_base_dir]
```

**Examples**:
```bash
# Single PDF
python 3_run_pipeline.py sample_manuals/manual.pdf data/output

# All PDFs in directory
python 3_run_pipeline.py sample_manuals/ data/output
```

**Output structure**:
```
data/output/
├── markdown/
│   ├── manual1.md
│   └── manual2.md
└── extracted/
    ├── manual1_extracted.json
    └── manual2_extracted.json
```

## Requirements

```bash
pip install docling pypdf
```

## Design Principles

- **Simple**: 3 scripts, clear responsibilities
- **Robust**: Error handling, validation, logging
- **POC-ready**: Works out of the box, no complex configuration
- **Extensible**: Easy to add more extraction patterns or processing steps

## Future Enhancements

Potential improvements (not implemented yet):
- LLM-based extraction for complex cases
- Multi-language support
- Image/diagram extraction
- Cross-reference resolution
- Semantic search indexing

## Testing

Test with the sample FANUC laser manual:

```bash
# Full pipeline
python 3_run_pipeline.py sample_manuals/ data/test_output

# Check outputs
cat data/test_output/markdown/*.md
cat data/test_output/extracted/*.json
```

## Troubleshooting

**Issue**: Docling takes too long
- **Solution**: This is normal for large PDFs. First run initializes models (~1-2 min), subsequent runs are faster.

**Issue**: No fault codes extracted
- **Solution**: Check the markdown output first. Extraction patterns may need tuning for your specific manual format.

**Issue**: PDF parsing artifacts in markdown
- **Solution**: The cleaning step should handle most artifacts. If issues persist, adjust the regex patterns in script 1.

## License

Part of the FactoryNet project.
