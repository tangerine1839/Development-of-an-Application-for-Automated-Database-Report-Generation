from typing import Optional, Literal

from pydantic import BaseModel


class InspectionItemCategory(BaseModel):
    id: int
    name: str
    type: Literal["Category"] = "Category"

    parent_id: int
    repeatable: bool
    parent_repeat_id: Optional[int] = None