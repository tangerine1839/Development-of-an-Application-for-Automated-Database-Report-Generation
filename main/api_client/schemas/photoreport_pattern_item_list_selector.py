from typing import List, Optional

from pydantic import BaseModel

from main.api_client.schemas.geo import Geo
from main.api_client.schemas.photoreport_item_trigger import PhotoreportItemTrigger


class PhotoreportPatternItemListSelector(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: int
    options: List[str] = []
    comment: Optional[str] = None
    triggers: List[PhotoreportItemTrigger] = []
    show_by_trigger: bool
    geo_auto: bool
    required: bool
    enabled: bool