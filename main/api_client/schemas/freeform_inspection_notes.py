from pydantic import BaseModel
from typing import Optional, List
from main.api_client.schemas.freeform_inspection_file import FreeformInspectionFile
from main.api_client.schemas.geo import Geo
from main.api_client.schemas.freeform_inspection_photo import FreeformInspectionPhoto
from main.api_client.schemas.freeform_inspection_video import FreeformInspectionVideo
from main.api_client.schemas.freeform_inspection_audio import FreeformInspectionAudio
from main.api_client.schemas.inspection_item_barcode import InspectionItemBarcode


class Category(BaseModel):
    id: str
    name: str


class LinkedTask(BaseModel):
    task_id: int
    is_violation: bool


class FreeformInspectionNotes(BaseModel):
    id: str
    title: str
    description: str
    category: Optional[Category] = None
    barcodes: List[InspectionItemBarcode] = []
    photos: List[FreeformInspectionPhoto] = []
    videos: List[FreeformInspectionVideo] = []
    audios: List[FreeformInspectionAudio] = []
    files: List[FreeformInspectionFile] = []
    linked_tasks: List[LinkedTask] = []
    geo: Optional[Geo] = None