from pydantic import BaseModel

class FreeformInspectionAudio(BaseModel):
    id: str
    url: str
    original_name: str
