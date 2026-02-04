from pydantic import BaseModel


class PhotoreportItemSection(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: str