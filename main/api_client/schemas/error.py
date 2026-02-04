from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class ValidationErrorDetail(BaseModel):
    key: str
    errors: List[str]


class Error(BaseModel):
    status: str = "error"
    message: Optional[str] = None
    validation_errors: Optional[List[ValidationErrorDetail]] = None