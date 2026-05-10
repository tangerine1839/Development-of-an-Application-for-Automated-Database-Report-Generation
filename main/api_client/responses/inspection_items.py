from typing import Optional

from pydantic import BaseModel

from main.api_client.schemas.inspection import Inspection
from main.api_client.schemas.task import Task


class InspectionItemsResponse(BaseModel):
    data: Inspection
    status: str = "success"
    message: Optional[str] = None
