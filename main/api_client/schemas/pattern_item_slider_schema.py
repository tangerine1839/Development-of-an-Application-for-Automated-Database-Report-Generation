from typing import List

from pydantic import BaseModel

from main.api_client.schemas.trigger import Trigger


class PatternItemSliderSchema(BaseModel):
    id: int
    name: str
    enabled: bool
    pattern_id: int
    description: str
    required: bool
    example_photos: List[str] = []
    include_in_email_report: bool
    triggers: List[Trigger] = []
    type: str
    min: int
    step: int
    max: int
