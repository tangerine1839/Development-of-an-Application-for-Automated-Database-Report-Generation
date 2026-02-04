from pydantic import BaseModel


class Pagination(BaseModel):
    total: int
    per_page: int
    current_page: int
    last_page: int
    from_: int
    to: int