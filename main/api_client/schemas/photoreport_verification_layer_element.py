from typing import Optional, List

from pydantic import BaseModel

from main.api_client.schemas.photoreport_decision_attach import PhotoreportDecisionAttach
from main.api_client.schemas.photoreport_graphic_note import PhotoreportGraphicNote


class PhotoreportVerificationLayerElement(BaseModel):
    item_id: int
    photo_id: int
    decision: Optional[str] = None
    comment: Optional[str] = None
    graphic_note: Optional[PhotoreportGraphicNote] = None
    attaches: List[PhotoreportDecisionAttach] = []