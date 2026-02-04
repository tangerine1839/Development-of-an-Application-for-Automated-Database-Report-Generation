from pydantic import BaseModel

class PermissionGroup(BaseModel):
    id: int
    name: str