from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PhotoreportPatternShort(BaseModel):
    id: int
    name: str
    color: str
    created_at: datetime
    updated_at: str
    instruction: Optional[str] = None
