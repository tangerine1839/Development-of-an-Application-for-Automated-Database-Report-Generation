from typing import List

from pydantic import BaseModel

from main.api_client.schemas.photoreport_photo_sample import PhotoreportPhotoSample


class PhotoreportItemInformation(BaseModel):
    id: int
    name: str
    description: str
    parent_id: int
    type: str
    show_by_trigger: bool
    is_shown: bool
    photo_samples: List[PhotoreportPhotoSample] = []

