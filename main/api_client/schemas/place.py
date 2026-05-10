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
    workingHours: Optional[str] = None
    additionalInfo: Optional[str] = None
    notWork: Optional[str] = None
    doNotShowInLists: Optional[bool] = None
    area: Optional[float] = None
    ceilingHeight: Optional[float] = None
    utcOffset: Optional[str] = None
    defaultPattern: Optional[int] = None
    defaultUser: Optional[int] = None
    emails: List[str] = []
    projectCustomer: Optional[str] = None
    projectDesigner: Optional[str] = None
    projectContractor: Optional[str] = None
    projectStaff: Optional[int] = None
    projectMachines: Optional[int] = None
    constructionStartAt: Optional[datetime] = None
    constructionFinishAt: Optional[datetime] = None
    responsibleUser: Optional[int] = None