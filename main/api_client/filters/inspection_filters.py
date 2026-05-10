from datetime import datetime
from typing import Optional, List, Literal
from pydantic import BaseModel

from main.api_client.schemas.inspection_short import InspectionShort

Status = Literal[
    "created",
    "completed",
    "process",
    "verification",
]

class TimeRange(BaseModel):
    from_: Optional[datetime] = None
    to: Optional[datetime] = None


class InspectionFilterSet(BaseModel):
    status: Optional[List[Status]] = None
    date: Optional[TimeRange] = None
    place_ids: Optional[List[int]] = None
    creator_ids: Optional[List[int]] = None
    assignee_ids: Optional[List[int]] = None
    is_guest: Optional[bool] = None

    def __eq__(self, other):
        if not isinstance(other, InspectionFilterSet):
            return False
        return (
            self.status == other.status
            and self.date == other.date
            and self.place_ids == other.place_ids
            and self.creator_ids == other.creator_ids
            and self.assignee_ids == other.assignee_ids
            and self.is_guest == other.is_guest
        )

    def __repr__(self):
        return (
            f"InspectionFilterSet("
            f"status={self.status}, "
            f"date={self.date}, "
            f"place_ids={self.place_ids}, "
            f"creator_ids={self.creator_ids}, "
            f"assignee_ids={self.assignee_ids}, "
            f"is_guest={self.is_guest})"
        )

    def build_query_params(self) -> dict:

        params = {}

        if self.status:
            params["i:statuses[]"] = self.status

        if self.date:
            if self.date.from_:
                params["i:date_from"] = self.date.from_.isoformat()
            if self.date.to:
                params["i:date_to"] = self.date.to.isoformat()

        if self.place_ids:
            params["i:places[]"] = self.place_ids

        if self.creator_ids:
            params["i:creators[]"] = self.creator_ids

        if self.assignee_ids:
            params["i:assignees[]"] = self.assignee_ids

        if self.is_guest is not None:
            params["i:is_guest"] = "true" if self.is_guest else "false"

        return params

    def filter_python(
            self,
            inspections: List["InspectionShort"],
    ) -> List["InspectionShort"]:

        filtered = []

        for inspection in inspections:

            if self.date:
                if self.date.from_ and inspection.date < self.date.from_:
                    continue
                if self.date.to and inspection.date > self.date.to:
                    continue
            filtered.append(inspection)

        return filtered