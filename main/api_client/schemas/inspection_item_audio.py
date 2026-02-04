from datetime import datetime
from pydantic import BaseModel


class InspectionItemAudio(BaseModel):
    id: int
    url: str
