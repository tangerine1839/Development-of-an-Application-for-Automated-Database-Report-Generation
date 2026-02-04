from typing import List, Optional

from pydantic import BaseModel

from main.api_client.schemas.geo import Geo
from main.api_client.schemas.photoreport_item_trigger import PhotoreportItemTrigger
from main.api_client.schemas.photoreport_photo import PhotoreportPhoto
from main.api_client.schemas.photoreport_photo_sample import PhotoreportPhotoSample


class PhotoreportItemPhoto(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: int
    options: List[str] = []
    answers: List[str] = []
    comment: Optional[str] = None
    show_by_trigger: bool
    triggers: List[PhotoreportItemTrigger] = []
    photo_samples: List[PhotoreportPhotoSample] = []
    photos: List[PhotoreportPhoto] = []
    geo: Optional[Geo] = None
    geo_auto: bool
