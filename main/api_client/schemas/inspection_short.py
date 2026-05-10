from datetime import datetime
from typing import Optional, List, Union

from pydantic import BaseModel

from main.api_client.schemas.guest_inspector import GuestInspector
from main.api_client.schemas.inspection_item_audio_type import InspectionItemAudioType
from main.api_client.schemas.inspection_item_category import InspectionItemCategory
from main.api_client.schemas.inspection_item_checkbox import InspectionItemCheckbox
from main.api_client.schemas.inspection_item_datetime import InspectionItemDateTime
from main.api_client.schemas.inspection_item_information import InspectionItemInformation
from main.api_client.schemas.inspection_item_list_selector import InspectionItemListSelector
from main.api_client.schemas.inspection_item_list_selector_multi import InspectionItemListSelectorMulti
from main.api_client.schemas.inspection_item_numeric_value import InspectionItemNumericValue
from main.api_client.schemas.inspection_item_photo_type import InspectionItemPhotoType
from main.api_client.schemas.inspection_item_section import InspectionItemSection
from main.api_client.schemas.inspection_item_signature import InspectionItemSignature
from main.api_client.schemas.inspection_item_slider import InspectionItemSlider
from main.api_client.schemas.inspection_item_text_comment import InspectionItemTextComment
from main.api_client.schemas.inspection_item_yes_no import InspectionItemYesNo
from main.api_client.schemas.pattern_short import PatternShort
from main.api_client.schemas.place import Place
from main.api_client.schemas.user_short import UserShort


class InspectionShort(BaseModel):
    id: int
    public_id: int
    status: Optional[str] = None
    date: Optional[datetime] = None
    deadline_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    stat_fails: Optional[int] = None
    stat_critical_fails: Optional[int] = None
    max_rate: Optional[int] = None
    factRate: Optional[int] = None
    place: Optional[Place] = None
    creator: Optional[UserShort] = None
    assignee: Optional[UserShort] = None
    pattern: Optional[PatternShort] = None
    force_complete: Optional[bool] = None
    blocked: Optional[bool] = None
    aborted: Optional[bool] = None
    guest_link: Optional[str] = None
    is_guest_inspection: Optional[bool] = None
    guest_inspector: Optional[GuestInspector] = None
    linear_filling: Optional[bool] = None
    deny_edit_answers: Optional[bool] = None
