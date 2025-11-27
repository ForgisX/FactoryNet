"""
LlamaIndex Experiments - Fault Extraction from PDF Manuals

This script extracts machine faults, root causes, and fixing steps from PDF manuals.
Uses Azure OpenAI for LLM-based extraction and pypdf for PDF parsing.
"""

import os
import json
import asyncio
from dotenv import load_dotenv
from pypdf import PdfReader
from llama_index.llms.azure_openai import AzureOpenAI

load_dotenv()

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

async def extract_metadata(text: str) -> dict:
    """Extract machine metadata from the manual."""
    print("Extracting Metadata...")
    
    prompt = f"""Extract the machine metadata from the following text and return ONLY a JSON object with these fields:
- manufacturer (string)
- model (string)
- series (string)
- description (string)

Text:
---------------------
{text[:2000]}
---------------------

Return only valid JSON, no other text."""

    response = await llm.acomplete(prompt)
    try:
        return json.loads(str(response))
    except json.JSONDecodeError as e:
        print(f"Failed to parse metadata JSON: {e}")
        print(f"Response was: {response}")
        return {"manufacturer": "Unknown", "model": "Unknown", "series": "Unknown", "description": ""}

async def extract_faults(text: str) -> list:
    """Extract faults, root causes, and fixing steps from the manual."""
    print("Extracting Faults...")
    
    prompt = f"""Extract all machine faults from the following manual text. Return ONLY a JSON array of fault objects.

Each fault object should have:
- fault_code (string): The error code
- fault_message (string): The error message
- root_causes (array): List of root cause objects
- source_chunk (string): Relevant excerpt from the manual

Each root_cause object should have:
- id (string): A unique identifier (e.g., "rc_001")
- description (string): Description of the root cause
- fixing_sequences (array): List of fixing sequence objects

Each fixing_sequence object should have:
- source (string): "manual" for now
- steps (array): List of step objects
- confidence_score (number): 1.0 for manual extraction

Each step object should have:
- order (number): Step number
- description (string): What to do

Text:
---------------------
{text[:15000]}
---------------------

Return only valid JSON array, no other text."""

    response = await llm.acomplete(prompt)
    try:
        result = json.loads(str(response))
        if isinstance(result, dict) and "faults" in result:
            return result["faults"]
        return result if isinstance(result, list) else []
    except json.JSONDecodeError as e:
        print(f"Failed to parse faults JSON: {e}")
        print(f"Response was: {response}")
        return []

async def main():
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, "sample_manuals", "B-70254EN_01_101028_fanuc_laser_digital.pdf")
    
    # Step 0: Parse PDF using pypdf
    print(f"Parsing {pdf_path} with pypdf...")
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n\n"
    print(f"Parsed {len(reader.pages)} pages, {len(full_text)} characters")
    
    # Step 0: Extract Metadata
    metadata = await extract_metadata(full_text)
    print("\n--- Metadata ---")
    print(json.dumps(metadata, indent=2))
    
    # Step 1 & 2: Extract Faults and Root Causes
    faults = await extract_faults(full_text)
    print(f"\n--- Extracted {len(faults)} faults ---")
    
    # Build databases
    fault_db = {}
    root_cause_db = {}
    
    for fault in faults:
        fault_code = fault.get("fault_code", "UNKNOWN")
        fault_db[fault_code] = {
            "fault_code": fault_code,
            "fault_message": fault.get("fault_message", ""),
            "source_chunk": fault.get("source_chunk", "")
        }
        
        for rc in fault.get("root_causes", []):
            rc_id = rc.get("id", f"rc_{len(root_cause_db)}")
            root_cause_db[rc_id] = rc
    
    # Save to files
    output_dir = "./manual_processing/data"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    
    with open(f"{output_dir}/fault_db.json", "w") as f:
        json.dump(fault_db, f, indent=2)
    
    with open(f"{output_dir}/root_cause_db.json", "w") as f:
        json.dump(root_cause_db, f, indent=2)
    
    print(f"\n--- Saved databases to {output_dir} ---")
    print(f"Metadata: {len(metadata)} fields")
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
    asyncio.run(main())
