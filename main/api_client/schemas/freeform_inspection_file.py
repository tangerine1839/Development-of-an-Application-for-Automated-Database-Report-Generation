from pydantic import BaseModel

class FreeformInspectionFile(BaseModel):
    id: str
    url: str
    original_name: str