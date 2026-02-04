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
    permission_group: Optional[PermissionGroup] = None
    position: str
    phone: str
    zone1: Zone
    zone2: Zone
    zone3: Zone
    places: List[Place] = []
    places_groups: List[PlaceGroup] = []
    notificable_places: List[Place] = []
    notificable_patterns: List[PatternShort] = []
    groups: List[UserGroup] = []
    notificable_new_tasks_priorities: str
    ldap_auth: bool
    ldap_login: Optional[bool] = None