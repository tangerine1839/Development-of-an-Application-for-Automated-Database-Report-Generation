from typing import List

from pydantic import BaseModel

from main.api_client.schemas.trigger import Trigger


class PatternItemListSelectorStore(BaseModel):
    id: int
    name: str
    enabled: bool
    type: str
    options: List[str] = []
    options_rates: List[str] = []