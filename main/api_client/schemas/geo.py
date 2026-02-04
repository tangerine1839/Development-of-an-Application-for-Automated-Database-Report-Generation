from pydantic import BaseModel


class Geo(BaseModel):
    lat: float
    lng: float