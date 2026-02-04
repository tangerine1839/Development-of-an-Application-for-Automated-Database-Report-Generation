from pydantic import BaseModel


class PhotoreportPatternItemSection(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: str
    enabled: bool