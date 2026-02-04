from pydantic import BaseModel

from main.api_client.schemas.user_short import UserShort


class PatternItemCategoryStore(BaseModel):
    name: str
    type: str
    pattern_id: int
    rate: int
    repeatable: bool
