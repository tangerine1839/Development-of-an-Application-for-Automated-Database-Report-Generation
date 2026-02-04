from datetime import datetime

from pydantic import BaseModel


class PhotoreportPhoto(BaseModel):
    id: int
    filename: str
    miniature: str
    source: str
    date: datetime
