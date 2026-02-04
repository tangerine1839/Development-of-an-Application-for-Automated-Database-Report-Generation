from typing import List

from pydantic import BaseModel

from main.api_client.schemas.trigger import Trigger


class PatternItemSliderStore(BaseModel):
    id: int
    name: str
    enabled: bool
    type: str
    min: int
    step: int
