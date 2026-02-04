from pydantic import BaseModel


class FreeformInspectionVideo(BaseModel):
    id: str
    url: str
    preview_url: str
    original_name: str