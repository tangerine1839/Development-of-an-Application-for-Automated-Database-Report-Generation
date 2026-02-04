from pydantic import BaseModel


class PhotoreportGraphicNote(BaseModel):
    id: int
    filename: str
    miniature: str