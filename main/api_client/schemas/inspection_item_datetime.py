from typing import Optional, List, Literal

from pydantic import BaseModel

from main.api_client.schemas.trigger import Trigger
from main.api_client.schemas.geo import Geo
from main.api_client.schemas.inspection_item_audio import InspectionItemAudio
from main.api_client.schemas.inspection_item_barcode import InspectionItemBarcode
from main.api_client.schemas.inspection_item_photo import InspectionItemPhoto
from main.api_client.schemas.inspection_item_video import InspectionItemVideo


class InspectionItemDateTime(BaseModel):
    id: int
    name: str
    type: Literal["DateTime"] = "DateTime"

    parent_id: int
    description: Optional[str] = None
    required: bool
    comment: Optional[str] = None
    photos: List[InspectionItemPhoto]
    barcodes: List[InspectionItemBarcode]
    audios: List[InspectionItemAudio]
    videos: List[InspectionItemVideo]
    example_photos: List[str]
    geo: Optional[Geo] = None

    geo_auto: bool
    value: Optional[str] = None
    show_by_trigger: bool
    value_type: Optional[str] = None
    triggers: List[Trigger] = []
    is_violated: bool
    factRate: int
    rate: int