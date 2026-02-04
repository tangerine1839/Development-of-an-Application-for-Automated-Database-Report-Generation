from pydantic import BaseModel


class Zone(BaseModel):
    id: int
    name: str