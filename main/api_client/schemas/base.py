from typing import TypeVar, Generic
from pydantic import BaseModel


DataT = TypeVar("DataT")


class Pagination(BaseModel):
    total: int
    per_page: int
    current_page: int
    last_page: int
    from_: int
    to: int
    status: str


class ApiResponse(BaseModel, Generic[DataT]):
    data: list[DataT]
    pagination: Pagination
