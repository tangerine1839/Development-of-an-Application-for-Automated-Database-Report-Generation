from typing import Optional, List

from pydantic import BaseModel


from main.api_client.schemas.trigger import Trigger, Action
from main.api_client.schemas.geo import Geo
from main.api_client.schemas.inspection_item_audio import InspectionItemAudio
from main.api_client.schemas.inspection_item_barcode import InspectionItemBarcode
from main.api_client.schemas.inspection_item_photo import InspectionItemPhoto
from main.api_client.schemas.inspection_item_video import InspectionItemVideo

class InspectionItemPhotoType(BaseModel):
    id: int
    name: str
    type: str
    parent_id: int
    description: Optional[str] = None
    required: bool
    comment: Optional[str] = None
    photos: List[InspectionItemPhoto] = []
    barcodes: List[InspectionItemBarcode] = []
    audios: List[InspectionItemAudio] = []
    videos: List[InspectionItemVideo] = []
    example_photos: List[str] = []
    geo: Geo
    geo_auto: bool
    show_by_trigger: bool
    triggers: List[Trigger] = []
    is_violated: bool