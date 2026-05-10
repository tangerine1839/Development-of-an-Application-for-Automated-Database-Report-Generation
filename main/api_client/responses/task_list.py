from typing import Optional

from pydantic import BaseModel, Field

from main.api_client.schemas.task_short import TaskShort
from main.api_client.schemas.base import ApiResponse, Pagination

class TaskListResponse(BaseModel):
    data: list[TaskShort]
    total: int
    per_page: int
    current_page: int
    last_page: int
    from_: Optional[int] = Field(alias="from")
    to: Optional[int] = None
    status: str = "success"
