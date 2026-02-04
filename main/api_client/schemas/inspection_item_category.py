from typing import Optional

from pydantic import BaseModel


class InspectionItemCategory(BaseModel):
    id: int
    name: str
    type: str
    parent_id: int
    repeatable: bool
    parent_repeat_id: Optional[int] = None