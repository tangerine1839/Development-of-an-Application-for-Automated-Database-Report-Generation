from pydantic import BaseModel


class GuestFormExtraFieldAnswer(BaseModel):
    key: str
    value: str