from llama_index.core.bridge.pydantic import BaseModel, Field
from typing import List

try:
    class Step(BaseModel):
        desc: str

    class Sequence(BaseModel):
        steps: List[Step]

    print("Pydantic V1 test passed")
except Exception as e:
    print(f"Pydantic V1 test failed: {e}")
