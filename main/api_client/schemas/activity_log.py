from datetime import datetime
from pydantic import BaseModel


class ActivityLog(BaseModel):
    id: int
    subject_type: str
    subject_id: int
    event: str
    causer_id: int
    created_at: datetime