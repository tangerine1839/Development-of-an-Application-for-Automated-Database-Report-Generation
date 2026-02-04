from typing import List, Optional

from pydantic import BaseModel

from main.api_client.schemas.geo import Geo
from main.api_client.schemas.photoreport_item_trigger import PhotoreportItemTrigger


class PhotoreportItemListSelector(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: int
    options: List[str] = []
    answers: List[str] = []
    comment: Optional[str] = None
    triggers: List[PhotoreportItemTrigger] = []
    show_by_trigger: bool
    is_shown: bool
    geo: Optional[Geo] = None
    geo_auto: bool
    required: bool