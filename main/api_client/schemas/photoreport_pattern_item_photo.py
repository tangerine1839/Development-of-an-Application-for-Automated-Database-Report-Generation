from typing import List

from pydantic import BaseModel

from main.api_client.schemas.photoreport_pattern_item_trigger import PhotoreportPatternItemTrigger
from main.api_client.schemas.photoreport_photo_sample import PhotoreportPhotoSample


class PhotoreportPatternItemPhoto(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: int
    show_by_trigger: bool
    geo_auto: bool
    triggers: List[PhotoreportPatternItemTrigger] = []
    photo_samples: List[PhotoreportPhotoSample] = []
    required: bool
    enabled: bool