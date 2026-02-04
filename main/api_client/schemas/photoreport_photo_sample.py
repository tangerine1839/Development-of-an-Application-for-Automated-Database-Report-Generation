from pydantic import BaseModel


class PhotoreportPhotoSample(BaseModel):
    id: int
    filename: str
    miniature: str