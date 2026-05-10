from typing import Optional

from pydantic import BaseModel

from main.api_client.schemas.permission_group import PermissionGroup


class UserShort(BaseModel):
    id: int
    name: str
    email: str
    role: str
    permission_group: Optional[PermissionGroup] = None
    position: str
    phone: Optional[str] = None