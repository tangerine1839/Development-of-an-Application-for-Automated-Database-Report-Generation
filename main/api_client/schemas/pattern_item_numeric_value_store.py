from typing import List, Optional

from pydantic import BaseModel


class PatternItemNumericValueStore(BaseModel):
    id: int
    name: str
    enabled: bool
    type: str
    postfix: str
    default: Optional[str] = None