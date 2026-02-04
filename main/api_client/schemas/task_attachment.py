from pydantic import BaseModel


class TaskAttachment(BaseModel):
    id: int
    display_name: str
    file_name: str