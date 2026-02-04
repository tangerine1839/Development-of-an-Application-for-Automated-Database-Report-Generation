from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from main.api_client.schemas.geo import Geo
from main.api_client.schemas.place_group import PlaceGroup
from main.api_client.schemas.zone import Zone




class Place(BaseModel):
    id: int
    name: str
    address: str
    geo: Optional[Geo] = None
    code: Optional[str] = None
    zone1: Optional[Zone] = None
    zone2: Optional[Zone] = None
    zone3: Optional[Zone] = None
    groups: List[PlaceGroup] = []
    manager: Optional[str] = None
    phone: Optional[str] = None
    working_hours: Optional[str] = None
    additional_info: Optional[str] = None
    not_work: Optional[str] = None
    do_not_show_in_lists: Optional[bool] = None
    area: Optional[float] = None
    ceiling_height: Optional[float] = None
    utc_offset: Optional[str] = None
    default_pattern: Optional[int] = None
    default_user: Optional[int] = None
    emails: List[str] = []
    project_customer: Optional[str] = None
    project_designer: Optional[str] = None
    project_contractor: Optional[str] = None
    project_staff: Optional[int] = None
    project_machines: Optional[int] = None
    construction_start_at: Optional[datetime] = None
    construction_finish_at: Optional[datetime] = None
    responsible_user: Optional[int] = None