from pydantic import BaseModel


class InspectionItemPhoto(BaseModel):
    id: int
    url: str