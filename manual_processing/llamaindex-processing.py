"""
LlamaIndex Experiments - Fault Extraction from PDF Manuals

This script extracts machine faults, root causes, and fixing steps from PDF manuals.
Uses Azure OpenAI for LLM-based extraction and pypdf for PDF parsing.
"""

import os
import json
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
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, "sample_manuals", "B-70254EN_01_101028_fanuc_laser_digital.pdf")
    pdf_path = os.path.join(script_dir, "sample_manuals", "B54810E_F1011_fanuc_scanned.pdf")
    
    # Step 0: Parse PDF using pypdf
    print(f"Parsing {pdf_path} with pypdf...")
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n\n"
    print(f"Parsed {len(reader.pages)} pages, {len(full_text)} characters")
    
    # Step 0: Extract Metadata
    metadata = extract_metadata(full_text)
    print("\n--- Metadata ---")
    print(metadata.model_dump_json(indent=2))
    
    # Step 1 & 2: Extract Faults and Root Causes
    fault_list = extract_faults(full_text)
    print(f"\n--- Extracted {len(fault_list.faults)} faults ---")
    
    # Build databases
    fault_db = {}
    root_cause_db = {}
    
    for fault in fault_list.faults:
        fault_db[fault.fault_code] = {
            "fault_code": fault.fault_code,
            "fault_message": fault.fault_message,
            "source_chunk": fault.source_chunk
        }
        
        for rc in fault.root_causes:
            root_cause_db[rc.id] = rc.model_dump()
    
    # Save to files
    output_dir = os.path.join(script_dir, "data")
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "metadata.json"), "w") as f:
        json.dump(metadata.model_dump(), f, indent=2)
    
    with open(os.path.join(output_dir, "fault_db.json"), "w") as f:
        json.dump(fault_db, f, indent=2)
    
    with open(os.path.join(output_dir, "root_cause_db.json"), "w") as f:
        json.dump(root_cause_db, f, indent=2)
    
    print(f"\n--- Saved databases to {output_dir} ---")
    print(f"Metadata: {len(metadata.model_dump())} fields")
    print(f"Fault DB: {len(fault_db)} faults")
    print(f"Root Cause DB: {len(root_cause_db)} root causes")
    
    # Print samples
    if fault_db:
        print("\n--- Fault DB Sample ---")
        print(json.dumps(list(fault_db.values())[:2], indent=2))
    
    if root_cause_db:
        print("\n--- Root Cause DB Sample ---")
        print(json.dumps(list(root_cause_db.values())[:2], indent=2))

if __name__ == "__main__":
    main()
