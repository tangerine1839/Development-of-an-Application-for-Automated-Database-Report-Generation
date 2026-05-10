from typing import Optional

from pydantic import BaseModel, Field

from main.api_client.schemas.user import User


class UserListResponse(BaseModel):
    data: list[User]
    total: int
    per_page: int
    current_page: int
    last_page: int
    from_: Optional[int] = Field(alias="from")
    to: Optional[int] = None
    status: str = "success"
