from datetime import datetime

from pydantic import BaseModel
from typing import Optional, List, Union

from main.api_client.schemas.photoreport_pattern_item_category import PhotoreportPatternItemCategory
from main.api_client.schemas.photoreport_pattern_item_information import PhotoreportPatternItemInformation
from main.api_client.schemas.photoreport_pattern_item_list_selector import PhotoreportPatternItemListSelector
from main.api_client.schemas.photoreport_pattern_item_photo import PhotoreportPatternItemPhoto
from main.api_client.schemas.photoreport_pattern_item_section import PhotoreportPatternItemSection
from main.api_client.schemas.photoreport_pattern_item_signature import PhotoreportPatternItemSignature


class PhotoreportPattern(BaseModel):
    id: int
    name: str
    color: str
    created_at: datetime
    updated_at: str
    instruction: Optional[str] = None
    items: List[Union[
        PhotoreportPatternItemSection,
        PhotoreportPatternItemCategory,
        PhotoreportPatternItemPhoto,
        PhotoreportPatternItemListSelector,
        PhotoreportPatternItemSignature,
        PhotoreportPatternItemInformation
    ]]