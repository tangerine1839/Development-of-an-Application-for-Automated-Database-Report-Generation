from pydantic import BaseModel


class PlaceGroup(BaseModel):
    id: int
    name: str