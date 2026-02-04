from pydantic import BaseModel

from main.api_client.schemas.user_short import UserShort


class PatternItemCategory(BaseModel):
    id: int
    name: str
    enabled: bool
    type: str
    pattern_id: int
    rate: int
    grant_access_and_notify: UserShort
    repeatable: bool
    