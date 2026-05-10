from typing import Optional

from pydantic import BaseModel

from main.api_client.schemas.task import Task


class TaskMessagesResponse(BaseModel):
    data: Task
    status: str = "success"
    message: Optional[str] = None
