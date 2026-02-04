from pydantic import BaseModel
from typing import Optional, List, Union
from datetime import datetime

from main.api_client.schemas.geo import Geo
from main.api_client.schemas.photoreport_item_category import PhotoreportItemCategory
from main.api_client.schemas.photoreport_item_information import PhotoreportItemInformation
from main.api_client.schemas.photoreport_item_list_selector import PhotoreportItemListSelector
from main.api_client.schemas.photoreport_item_photo import PhotoreportItemPhoto
from main.api_client.schemas.photoreport_item_section import PhotoreportItemSection
from main.api_client.schemas.photoreport_item_signature import PhotoreportItemSignature
from main.api_client.schemas.photoreport_pattern_short import PhotoreportPatternShort
from main.api_client.schemas.photoreport_verification_layer_element import PhotoreportVerificationLayerElement
from main.api_client.schemas.place import Place
from main.api_client.schemas.user_short import UserShort


class Photoreport(BaseModel):
    id: int
    public_id: int
    start_at: datetime
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    deadline_at: datetime
    status: str
    guest_link: str
    max_rate: int
    fact_rate: int
    stat_fail: int
    device: str
    created_at: datetime
    updated_at: datetime
    start_notify_m: Optional[int] = None
    deadline_notify_m: Optional[int] = None
    assignee: UserShort
    validator: UserShort
    place: Place
    pattern: PhotoreportPatternShort
    creator: UserShort
    geo_start: Optional[Geo] = None
    geo_finish: Optional[Geo] = None
    comment: str
    items: List[Union[
        PhotoreportItemSection,
        PhotoreportItemCategory,
        PhotoreportItemPhoto,
        PhotoreportItemListSelector,
        PhotoreportItemSignature,
        PhotoreportItemInformation
    ]]
    verification: List[PhotoreportVerificationLayerElement]