from datetime import datetime
from typing import List

from pydantic import BaseModel

from main.api_client.schemas.task_attachment import TaskAttachment
from main.api_client.schemas.user_short import UserShort


class TaskMessage(BaseModel):
    id: int
    user: UserShort
    message: str
    created_at: datetime
    attaches: List[TaskAttachment] = []