from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from main.api_client.schemas.inspection import Inspection
from main.api_client.schemas.inspection_short import InspectionShort
from main.api_client.schemas.place import Place
from main.api_client.schemas.task_message import TaskMessage
from main.api_client.schemas.user_short import UserShort

class Category(BaseModel):
    id: int
    name: str

class Task(BaseModel):
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
    place: Optional[Place] = None
    inspection: Optional[InspectionShort] = None
    item_id: Optional[int] = None
    messages: List[TaskMessage] = []
    rules: List[str] = []
    categories: List[Category] = []
