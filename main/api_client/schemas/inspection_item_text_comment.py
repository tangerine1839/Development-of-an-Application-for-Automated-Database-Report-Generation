from typing import Optional, List, Literal

from pydantic import BaseModel


from main.api_client.schemas.trigger import Trigger, Action
from main.api_client.schemas.geo import Geo
from main.api_client.schemas.inspection_item_audio import InspectionItemAudio
from main.api_client.schemas.inspection_item_barcode import InspectionItemBarcode
from main.api_client.schemas.inspection_item_photo import InspectionItemPhoto
from main.api_client.schemas.inspection_item_video import InspectionItemVideo

class InspectionItemTextComment(BaseModel):
    id: int
    name: str
    type: Literal["TextComment"] = "TextComment"

    parent_id: int
    description: Optional[str] = None
    required: bool
    photos: List[InspectionItemPhoto] = []
    barcodes: List[InspectionItemBarcode] = []
    audios: List[InspectionItemAudio] = []
    videos: List[InspectionItemVideo] = []
    example_photos: List[str] = []
    geo: Optional[Geo] = None

    geo_auto: bool
    value: Optional[str] = None
    show_by_trigger: bool
    comment: Optional[str] = None
    triggers: List[Trigger] = []
    is_violated: bool