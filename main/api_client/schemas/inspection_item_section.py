from typing import Literal

from pydantic import BaseModel


class InspectionItemSection(BaseModel):
    id: int
    name: str
    type: Literal["Section"] = "Section"
