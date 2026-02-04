from pydantic import BaseModel


class InspectionItemSection(BaseModel):
    id: int
    name: str
    type: str