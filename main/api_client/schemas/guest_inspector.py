from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from main.api_client.schemas.guest_form_extra_field_answer import GuestFormExtraFieldAnswer

class GuestInspector(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    extra_fields: List[GuestFormExtraFieldAnswer] = []
    created_at: datetime
    updated_at: datetime