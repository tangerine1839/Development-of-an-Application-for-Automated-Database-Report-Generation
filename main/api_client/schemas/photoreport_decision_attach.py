from pydantic import BaseModel


class PhotoreportDecisionAttach(BaseModel):
    id: int
    display_name: str
    filename: str
    mime_type: str
    file_size: int