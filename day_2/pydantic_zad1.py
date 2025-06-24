from pydantic import BaseModel
from typing import List, Dict


#  uv pip install pydantic

class Payload(BaseModel):
    names: List[str]
    options: Dict[str, int]


data = {
    "names": ["Ala", "Ola"],
    "options": {"limit": 10, "offset": 5}
}

payload = Payload(**data)
print(payload)  # names=['Ala', 'Ola'] options={'limit': 10, 'offset': 5}

data = {
    "names": ["Ala", 123],
    "options": {"limit": 10, "offset": 5}
}
# payload = Payload(**data) # pydantic_core._pydantic_core.ValidationError: 1 validation error for Payload
