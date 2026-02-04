from pydantic import BaseModel


class PatternItemTextCommentStore(BaseModel):
    id: str
    name: str
    enabled: bool
    type: str
