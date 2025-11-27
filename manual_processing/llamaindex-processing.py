"""
LlamaIndex Experiments - Fault Extraction from PDF Manuals

This script extracts machine faults, root causes, and fixing steps from PDF manuals.
Uses Azure OpenAI for LLM-based extraction and pypdf for PDF parsing.
"""

import os
import json
import argparse
import time
from pathlib import Path
from tqdm import tqdm
from datetime import datetime
import asyncio
from typing import List
from dotenv import load_dotenv
from pypdf import PdfReader
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.core.bridge.pydantic import BaseModel
from llama_index.core.program import LLMTextCompletionProgram

load_dotenv()

# --- Data Models ---

class MachineMetadata(BaseModel):
    """Metadata about the machine from the manual."""
    manufacturer: str
    model: str
    series: str
    description: str

class FixingStep(BaseModel):
    """A single step in a fixing sequence."""
    order: int
    description: str

class FixingSequence(BaseModel):
    """A sequence of steps to fix a root cause."""
    source: str  # "manual", "online", or "hybrid"
    steps: List[FixingStep]
    confidence_score: float

class RootCause(BaseModel):
    """A root cause for a machine fault."""
    id: str
    description: str
    fixing_sequences: List[FixingSequence]

class MachineFault(BaseModel):
    """A machine fault with its root causes."""
    fault_code: str
    fault_message: str
    root_causes: List[RootCause]
    source_chunk: str

class FaultList(BaseModel):
    """Container for multiple faults."""
    faults: List[MachineFault]

# --- Setup ---

llm = AzureOpenAI(
    model="gpt-4",
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0
)

# --- Extraction Functions ---

def extract_metadata(text: str) -> MachineMetadata:
    """Extract machine metadata from the manual using structured output."""
    print("Extracting Metadata...")
    
    prompt_template_str = """Extract the machine metadata from the following text.

Text:
---------------------
{text}
---------------------

Provide the manufacturer, model, series, and a brief description."""

    program = LLMTextCompletionProgram.from_defaults(
        output_cls=MachineMetadata,
        llm=llm,
        prompt_template_str=prompt_template_str,
        verbose=True
    )
    
    return program(text=text[:2000])

def extract_faults(text: str) -> FaultList:
    """Extract faults, root causes, and fixing steps using structured output."""
    print("Extracting Faults...")
    
    prompt_template_str = """Extract all machine faults from the following manual text.

For each fault, identify:
- The fault code and message
- All possible root causes
- For each root cause, provide fixing steps
- Mark the source as "manual"
- Include a relevant excerpt in source_chunk

Text:
---------------------
{text}
---------------------

Extract all faults with their root causes and fixing sequences."""

    program = LLMTextCompletionProgram.from_defaults(
        output_cls=FaultList,
        llm=llm,
        prompt_template_str=prompt_template_str,
        verbose=True
    )
    
    return program(text=text[:15000])

def main():
    # CLI args
    parser = argparse.ArgumentParser(description="Extract faults and metadata from a PDF manual using LlamaIndex (Azure OpenAI)")
    parser.add_argument("pdf", nargs="?", default=None, help="Path to the input PDF manual (optional, defaults to sample laser manual)")
    parser.add_argument("--out", dest="out_dir", default=None, help="Optional output directory. Defaults to manual_processing/data/llamaindex_outputs/<pdf_stem>/<timestamp>/")
    args = parser.parse_args()

    # Resolve paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if args.pdf is None:
        default_pdf = os.path.join(script_dir, "sample_manuals", "B-70254EN_01_101028_fanuc_laser_digital.pdf")
        pdf_path = os.path.abspath(default_pdf)
        print(f"No PDF argument supplied. Using default: {pdf_path}")
    else:
        pdf_path = os.path.abspath(args.pdf)
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    
    # Step 0: Parse PDF using pypdf
    print(f"Parsing {pdf_path} with pypdf...")
    parse_start = time.perf_counter()
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in tqdm(reader.pages, desc="Pages", unit="page"):
        page_text = page.extract_text() or ""
        full_text += page_text + "\n\n"
    parse_elapsed = time.perf_counter() - parse_start
    print(f"Parsed {len(reader.pages)} pages, {len(full_text)} characters in {parse_elapsed:.2f}s")
    
    # Step 0: Extract Metadata
    meta_start = time.perf_counter()
    metadata = extract_metadata(full_text)
    meta_elapsed = time.perf_counter() - meta_start
    print("\n--- Metadata ---")
    print(metadata.model_dump_json(indent=2))
    print(f"Metadata extraction time: {meta_elapsed:.2f}s")
    
    # Step 1 & 2: Extract Faults and Root Causes
    faults_start = time.perf_counter()
    fault_list = extract_faults(full_text)
    faults_elapsed = time.perf_counter() - faults_start
    print(f"\n--- Extracted {len(fault_list.faults)} faults ---")
    print(f"Fault extraction time: {faults_elapsed:.2f}s")
    
    # Build databases
    fault_db = {}
    root_cause_db = {}
    
    build_start = time.perf_counter()
    for fault in tqdm(fault_list.faults, desc="Faults", unit="fault"):
        fault_db[fault.fault_code] = {
            "fault_code": fault.fault_code,
            "fault_message": fault.fault_message,
            "source_chunk": fault.source_chunk
        }
        for rc in fault.root_causes:
            root_cause_db[rc.id] = rc.model_dump()
    build_elapsed = time.perf_counter() - build_start
    
    # Save to files
    if args.out_dir:
        output_dir = os.path.abspath(args.out_dir)
    else:
        pdf_stem = Path(pdf_path).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join(script_dir, "data", "llamaindex_outputs", pdf_stem, timestamp)
    os.makedirs(output_dir, exist_ok=True)

    # Save raw manual text as markdown
    markdown_path = os.path.join(output_dir, f"{Path(pdf_path).stem}.md")
    with open(markdown_path, "w", encoding="utf-8") as f_md:
        f_md.write(f"# Manual: {Path(pdf_path).name}\n\n")
        f_md.write(full_text)
    print(f"Saved markdown to {markdown_path}")
    
    save_start = time.perf_counter()
    with open(os.path.join(output_dir, "metadata.json"), "w") as f:
        json.dump(metadata.model_dump(), f, indent=2)
    
    with open(os.path.join(output_dir, "fault_db.json"), "w") as f:
        json.dump(fault_db, f, indent=2)
    
    with open(os.path.join(output_dir, "root_cause_db.json"), "w") as f:
        json.dump(root_cause_db, f, indent=2)
    save_elapsed = time.perf_counter() - save_start
    
    print(f"\n--- Saved databases to {output_dir} ---")
    print(f"Markdown file: {markdown_path}")
    print(f"Metadata: {len(metadata.model_dump())} fields ( {meta_elapsed:.2f}s )")
    print(f"Fault DB: {len(fault_db)} faults (extract {faults_elapsed:.2f}s, build {build_elapsed:.2f}s)")
    print(f"Root Cause DB: {len(root_cause_db)} root causes")
    print(f"File save time: {save_elapsed:.2f}s")
    total_elapsed = parse_elapsed + meta_elapsed + faults_elapsed + build_elapsed + save_elapsed
    print(f"Total processing time: {total_elapsed:.2f}s")
    
    # Print samples
    if fault_db:
        print("\n--- Fault DB Sample ---")
        print(json.dumps(list(fault_db.values())[:2], indent=2))
    
    if root_cause_db:
        print("\n--- Root Cause DB Sample ---")
        print(json.dumps(list(root_cause_db.values())[:2], indent=2))

if __name__ == "__main__":
    main()
