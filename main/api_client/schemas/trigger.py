from typing import Optional, List

from pydantic import BaseModel


class Action(BaseModel):
    type: str
    item_id: Optional[int] = None
    evidence_count: Optional[int] = None
    evidence_max: Optional[int] = None

class Trigger(BaseModel):
    condition: str
    values: List[str]
    actions: List[Action]