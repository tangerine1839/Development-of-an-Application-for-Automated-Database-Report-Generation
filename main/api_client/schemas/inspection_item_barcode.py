from pydantic import BaseModel


class InspectionItemBarcode(BaseModel):
    id: str
    barcode: str