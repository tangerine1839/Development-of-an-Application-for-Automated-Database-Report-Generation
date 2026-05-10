from typing import Optional, List, Literal

from pydantic import BaseModel

from main.api_client.schemas.trigger import Trigger, Action
from main.api_client.schemas.geo import Geo
from main.api_client.schemas.inspection_item_audio import InspectionItemAudio
from main.api_client.schemas.inspection_item_barcode import InspectionItemBarcode
from main.api_client.schemas.inspection_item_photo import InspectionItemPhoto
from main.api_client.schemas.inspection_item_video import InspectionItemVideo


class InspectionItemAudioType(BaseModel):
    id: int
    name: str
    type: Literal["AudioType"] = "AudioType"
    parent_id: int
    description: Optional[str] = None
    required: bool
    comment: Optional[str] = None
    photos: List[InspectionItemPhoto] = []
    barcodes: List[InspectionItemBarcode] = []
    audios: List[InspectionItemAudio] = []
    videos: List[InspectionItemVideo] = []
    example_photos: List[str] = []
    geo: Optional[Geo] = None
    geo_auto: bool
    show_by_trigger: bool
    triggers: List[Trigger] = []
    is_violated: bool