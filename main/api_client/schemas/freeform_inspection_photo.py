from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class FreeformInspectionPhoto(BaseModel):
    id: str
    url: str
    miniature: str
    created_at: datetime
    created_at_from_meta: Optional[datetime] = None
    created_at_from_device: Optional[datetime] = None
    source: str