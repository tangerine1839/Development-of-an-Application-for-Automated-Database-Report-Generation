from datetime import datetime
from typing import List

from pydantic import BaseModel

from main.api_client.schemas.pattern_item import PatternItem


class Pattern(BaseModel):
    id: int
    name: str
    color: str
    created_at: datetime
    updated_at: datetime
    instruction: str
    nothing_value_rated_as_positive: bool
    allow_upload_photos_from_phone_gallery: bool
    items: List[PatternItem] = []

