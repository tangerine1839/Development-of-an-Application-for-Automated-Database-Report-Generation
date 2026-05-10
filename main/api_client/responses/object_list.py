# В файле webapp/api_client/schemas/object.py
from typing import Optional, List
from pydantic import BaseModel, Field
from main.api_client.schemas.place import Place

class ObjectListData(BaseModel):
    total: int
    per_page: int
    current_page: int
    last_page: int
    from_: Optional[int] = Field(alias="from")
    to: Optional[int] = None
    data: List[Place]

    class Config:
        populate_by_name = True

class ObjectListResponse(BaseModel):
    data: ObjectListData
    status: str = "success"