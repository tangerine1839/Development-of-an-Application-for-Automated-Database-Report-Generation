from pydantic import BaseModel


class PhotoreportPatternItemCategory(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: str
    repeatable: bool
    enabled: bool