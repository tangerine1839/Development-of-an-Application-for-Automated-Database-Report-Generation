from pydantic import BaseModel


class TaskAttachment(BaseModel):
    id: int
    display_name: str
    filename: str