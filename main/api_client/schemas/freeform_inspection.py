from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from main.api_client.schemas.geo import Geo
from main.api_client.schemas.place import Place
from main.api_client.schemas.user_short import UserShort


class FreeformInspection(BaseModel):
    id: str
    place: Place
    creator: UserShort
    assignee: UserShort
    public_id: int
    status: str
    name: str
    description: str
    members: List[UserShort]
    geo_required: bool
    read_geo_for_notice: bool
    allow_upload_photos_from_phone_gallery: bool
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    device: str
    geo_started_at: Optional[Geo] = None
    geo_completed_at: Optional[Geo] = None
    notes_count: int