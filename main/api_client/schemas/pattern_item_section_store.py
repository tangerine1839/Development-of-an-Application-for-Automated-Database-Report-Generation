from pydantic import BaseModel


class PatternItemSectionStore(BaseModel):
    name: str
    type: str