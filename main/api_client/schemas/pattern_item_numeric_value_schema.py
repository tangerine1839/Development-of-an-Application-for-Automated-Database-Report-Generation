from typing import List, Optional

from pydantic import BaseModel

from main.api_client.schemas.trigger import Trigger


class PatternItemNumericValueSchema(BaseModel):
    id: int
    name: str
    enabled: bool
    pattern_id: int
    description: str
    required: bool
    example_photos: List[str] = []
    include_in_email_report: bool
    triggers: List[Trigger] = []
    type: str
    postfix: str
    default: Optional[str] = None