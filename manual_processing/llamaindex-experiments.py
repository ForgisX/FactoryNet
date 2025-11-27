import os
import json
import asyncio
from typing import List, Optional, Literal
from dotenv import load_dotenv
from llama_index.core.bridge.pydantic import BaseModel, Field
from llama_parse import LlamaParse
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.core.program import LLMTextCompletionProgram

load_dotenv()

# --- Data Models ---

class MachineMetadata(BaseModel):
    manufacturer: str
    model: str
    series: str
    description: str

class FixingStep(BaseModel):
    order: int
    description: str

class FixingSequence(BaseModel):
    source: str
    steps: List[FixingStep]
    confidence_score: float

class RootCause(BaseModel):
    id: str
    description: str
    fixing_sequences: List[FixingSequence]

class MachineFault(BaseModel):
    fault_code: str
    fault_message: str
    root_causes: List[RootCause]
    source_chunk: str

class FaultList(BaseModel):
    faults: List[MachineFault]

# --- Setup ---

llm = AzureOpenAI(
    model="gpt-4",
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4"), # Fallback or env var
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0
)

parser = LlamaParse(
    api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
    result_type="markdown",
    verbose=True,
    language="en",
)

# --- Extraction Functions ---

async def extract_metadata(markdown_text: str) -> MachineMetadata:
    print("Extracting Metadata...")
    prompt_template_str = (
        "Extract the machine metadata from the following text:\n"
        "---------------------\n"
        "{text}\n"
        "---------------------\n"
    )
    program = LLMTextCompletionProgram.from_defaults(
        output_cls=MachineMetadata,
        llm=llm,
        prompt_template_str=prompt_template_str,
    )
    # Use first 2000 chars for metadata extraction as it's usually at the top
    return program(text=markdown_text[:2000])

async def extract_faults(markdown_text: str) -> List[MachineFault]:
    print("Extracting Faults (Step 1)...")
    # Simple chunking by "Number" or "Message" keywords often found in Fanuc manuals
    # For now, we'll just pass the whole text if it's small, or chunk it blindly.
    # Given the sample might be large, let's try to split by some heuristic or just use a large context window.
    # For this POC, we'll assume the relevant section is passed or we split by pages.
    
    # Heuristic: Split by "Number" if possible, or just arbitrary chunks.
    # Let's try to extract from the whole text for the POC, assuming it fits in context (GPT-4 128k).
    # If not, we'd iterate.
    
    prompt_template_str = (
        "Extract all machine faults, their root causes, and fixing steps from the following text.\n"
        "For each fault, include the original text chunk where it was found in 'source_chunk'.\n"
        "Tag the fixing sequence source as 'manual'.\n"
        "---------------------\n"
        "{text}\n"
        "---------------------\n"
    )
    
    # We use a list container to extract multiple
    program = LLMTextCompletionProgram.from_defaults(
        output_cls=FaultList,
        llm=llm,
        prompt_template_str=prompt_template_str,
    )
    
    # In a real scenario, we would iterate over chunks. 
    # Here we pass the text. If it's too long, we might need to truncate or chunk.
    # Let's assume the sample is manageable or we take a significant portion.
    result = program(text=markdown_text)
    return result.faults

async def main():
    pdf_path = "./sample_manuals/B-70254EN_01_101028_fanuc_laser_digital.pdf"
    
    # 1. Parse
    print(f"Parsing {pdf_path}...")
    documents = await parser.aload_data(pdf_path)
    full_markdown = "\n\n".join([doc.text for doc in documents])
    
    # 2. Metadata
    metadata = await extract_metadata(full_markdown)
    print("Metadata Extracted:", metadata.model_dump_json(indent=2))
    
    # 3. Fault Extraction (Step 1 & 2 combined in one LLM call for POC efficiency, 
    # but logically distinct in data model)
    # Note: The prompt asks for root causes too, covering Step 2.
    faults = await extract_faults(full_markdown)
    
    # 4. Output
    print(f"Extracted {len(faults)} faults.")
    
    # Transform to DB structure
    fault_db = {}
    root_cause_db = {}
    
    for fault in faults:
        fault_db[fault.fault_code] = fault.model_dump(exclude={"root_causes"})
        for rc in fault.root_causes:
            root_cause_db[rc.id] = rc.model_dump()
            
    print("\n--- Fault DB Sample ---")
    print(json.dumps(list(fault_db.values())[:2], indent=2))
    
    print("\n--- Root Cause DB Sample ---")
    print(json.dumps(list(root_cause_db.values())[:2], indent=2))

if __name__ == "__main__":
    print("Instantiating models...")
    try:
        m = MachineMetadata(manufacturer="Fanuc", model="Laser", series="C", description="A laser machine")
        print("Metadata instantiated")
        fs = FixingStep(order=1, description="Fix it")
        seq = FixingSequence(source="manual", steps=[fs], confidence_score=1.0)
        rc = RootCause(id="rc1", description="Broken", fixing_sequences=[seq])
        mf = MachineFault(fault_code="101", fault_message="Error", root_causes=[rc], source_chunk="chunk")
        fl = FaultList(faults=[mf])
        print("All models instantiated successfully")
    except Exception as e:
        print(f"Model instantiation failed: {e}")
        exit(1)
    
    # asyncio.run(main())
