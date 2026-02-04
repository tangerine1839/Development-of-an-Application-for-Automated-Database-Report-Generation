from typing import List

from pydantic import BaseModel

class Action(BaseModel):
    type: str
    item_id: str


class PhotoreportPatternItemTrigger(BaseModel):
    values: List[str] = []
    actions: List[Action] = []
    condition: str
