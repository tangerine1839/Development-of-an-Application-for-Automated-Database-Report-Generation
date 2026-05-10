from datetime import datetime
from typing import Optional, List, Union, Annotated

from pydantic import BaseModel, Field

from main.api_client.schemas.guest_inspector import GuestInspector
from main.api_client.schemas.inspection_item_audio_type import InspectionItemAudioType
from main.api_client.schemas.inspection_item_category import InspectionItemCategory
from main.api_client.schemas.inspection_item_checkbox import InspectionItemCheckbox
from main.api_client.schemas.inspection_item_datetime import InspectionItemDateTime
from main.api_client.schemas.inspection_item_information import InspectionItemInformation
from main.api_client.schemas.inspection_item_list_selector import InspectionItemListSelector
from main.api_client.schemas.inspection_item_list_selector_multi import InspectionItemListSelectorMulti
from main.api_client.schemas.inspection_item_numeric_value import InspectionItemNumericValue
from main.api_client.schemas.inspection_item_photo_new import InspectionItemPhotoNew
from main.api_client.schemas.inspection_item_photo_type import InspectionItemPhotoType
from main.api_client.schemas.inspection_item_section import InspectionItemSection
from main.api_client.schemas.inspection_item_signature import InspectionItemSignature
from main.api_client.schemas.inspection_item_slider import InspectionItemSlider
from main.api_client.schemas.inspection_item_text_comment import InspectionItemTextComment
from main.api_client.schemas.inspection_item_yes_no import InspectionItemYesNo
from main.api_client.schemas.pattern_short import PatternShort
from main.api_client.schemas.place import Place
from main.api_client.schemas.user_short import UserShort


class Inspection(BaseModel):
    id: int
    public_id: int
    status: str
    date: str
    deadline_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    stat_fails: Optional[int] = None
    stat_critical_fails: Optional[int] = None
    max_rate: Optional[int] = None
    fact_rate: int
    place: Place
    creator: UserShort
    assignee: UserShort
    pattern: PatternShort
    force_complete: bool
    blocked: bool
    aborted: bool
    guest_link: str
    is_guest_inspection: bool
    guest_inspector: Optional[GuestInspector] = None
    linear_filling: bool
    deny_edit_answers: bool
    items: List[Annotated[Union[
        InspectionItemPhotoNew,
        InspectionItemSection,
        InspectionItemCategory,
        InspectionItemYesNo,
        InspectionItemSlider,
        InspectionItemListSelector,
        InspectionItemNumericValue,
        InspectionItemTextComment,
        InspectionItemAudioType,
        InspectionItemCheckbox,
        InspectionItemSignature,
        InspectionItemPhotoType,
        InspectionItemInformation,
        InspectionItemDateTime,
        InspectionItemListSelectorMulti
    ],         Field(discriminator="type")
]] = []