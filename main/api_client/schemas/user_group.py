from pydantic import BaseModel


class UserGroup(BaseModel):
    id: int
    name: str