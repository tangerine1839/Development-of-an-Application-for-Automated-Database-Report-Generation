from pydantic import BaseModel


class PatternItemSection(BaseModel):
    id: int
    name: str
    enabled: bool
    type: str