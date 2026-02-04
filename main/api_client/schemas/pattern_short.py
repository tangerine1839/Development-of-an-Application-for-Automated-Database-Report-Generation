from datetime import datetime

from pydantic import BaseModel


class PatternShort(BaseModel):
    id: int
    name: str
    color: str
    created_at: datetime
    updated_at: datetime
    instruction: str
    nothing_value_rated_as_positive: bool
    allow_upload_photos_from_phone_gallery: bool