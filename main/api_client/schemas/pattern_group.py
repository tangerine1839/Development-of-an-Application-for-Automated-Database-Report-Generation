from pydantic import BaseModel


class PatternGroup(BaseModel):
    id: int
    name: str