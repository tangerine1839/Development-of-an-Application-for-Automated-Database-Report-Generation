from re import Pattern
from typing import Optional, List

from pydantic import BaseModel

from main.api_client.schemas.pattern_short import PatternShort
from main.api_client.schemas.permission_group import PermissionGroup
from main.api_client.schemas.place import Place
from main.api_client.schemas.place_group import PlaceGroup
from main.api_client.schemas.user_group import UserGroup
from main.api_client.schemas.zone import Zone


class User(BaseModel):
    id: int
    name: str
    email: str
    role: str
    permissionGroup: Optional[PermissionGroup] = None
    position: str
    phone: Optional[str] = None
    zone1: Optional[List[Zone]] = None
    zone2: Optional[List[Zone]] = None
    zone3: Optional[List[Zone]] = None
    places: Optional[List[Place]] = None
    placesGroups: List[PlaceGroup] = []
    notificablePlaces: List[Place] = []
    notificablePatterns: List[PatternShort] = []
    groups: List[UserGroup] = []
    notificableNewTasksPriorities: Optional[List[str]] = None
    ldapAuth: bool
    ldapLogin: Optional[bool] = None