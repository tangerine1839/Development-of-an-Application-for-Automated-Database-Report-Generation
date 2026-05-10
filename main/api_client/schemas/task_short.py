from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from main.api_client.schemas.user_short import UserShort


class TaskShort(BaseModel):
    id: int
    public_id: int
    inspection_id: Optional[int] = None
    status: str
    title: str
    description: str
    creator: UserShort
    assignee: UserShort
    validator: Optional[UserShort] = None
    priority: str
    created_at: datetime
    expire_at: datetime
    finished_at: Optional[datetime] = None