from typing import List, Optional

from pydantic import BaseModel

from main.api_client.schemas.geo import Geo
from main.api_client.schemas.photoreport_item_trigger import PhotoreportItemTrigger
from main.api_client.schemas.photoreport_photo import PhotoreportPhoto


class PhotoreportItemSignature(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: int
    show_by_trigger: bool
    is_shown: bool
    triggers: List[PhotoreportItemTrigger] = []
    signature: Optional[PhotoreportPhoto] = None
    geo: Optional[Geo] = None
    geo_auto: bool
    required: bool
