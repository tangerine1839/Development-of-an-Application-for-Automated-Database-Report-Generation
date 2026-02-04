from typing import Optional

from pydantic import BaseModel


class PhotoreportItemCategory(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: str
    repeatable: bool
    parent_repeat_id: Optional[int] = None