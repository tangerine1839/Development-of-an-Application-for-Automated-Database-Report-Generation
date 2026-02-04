from pydantic import BaseModel


class InspectionItemVideo(BaseModel):
    id: int
    url: str
    preview_url: str