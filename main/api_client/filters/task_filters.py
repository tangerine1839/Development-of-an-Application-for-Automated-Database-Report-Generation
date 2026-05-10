from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel

from main.api_client.schemas.task_short import TaskShort

Status = Literal[
    "completed",
    "created",
    "process",
    "revise",
    "review",
    "validation",
    "archived",
    "manual_review",
    "cancelled",
]

class TimeRange(BaseModel):

    from_: Optional[datetime] = None
    to: Optional[datetime] = None

class TaskFilterSet(BaseModel):

    status: Optional[List[Status]] = None
    created_at: Optional[TimeRange] = None
    finished_at: Optional[TimeRange] = None
    creator_id: Optional[List[str]] = None
    assignee_id: Optional[List[str]] = None

    def __eq__(self, other):
        if not isinstance(other, TaskFilterSet):
            return False
        return (
            self.status == other.status
            and self.created_at == other.created_at
            and self.finished_at == other.finished_at
            and self.creator_id == other.creator_id
            and self.assignee_id == other.assignee_id
        )

    def __repr__(self):
        return (
            f"TaskFilterSet("
            f"status={self.status}, "
            f"created_at={self.created_at}, "
            f"finished_at={self.finished_at})"
        )

    def build_query_params(self) -> dict:

        params = {}

        if self.status:

            params["t:statuses[]"] = self.status

        if self.creator_id:
            params["t:creators[]"] = self.creator_id
        if self.assignee_id:
            params["t:assignees[]"] = self.assignee_id
        if self.created_at:
            if self.created_at.from_:
                params["t:created_at_from"] = self.created_at.from_.isoformat()
            if self.created_at.to:
                params["t:created_at_to"] = self.created_at.to.isoformat()

        if self.finished_at:
            if self.finished_at.from_:
                params["t:finished_at_from"] = self.finished_at.from_.isoformat()
            if self.finished_at.to:
                params["t:finished_at_to"] = self.finished_at.to.isoformat()

        return params

    def filter_python(
            self,
            tasks: List[TaskShort],
    ) -> List[TaskShort]:

        filtered = []
        if not self.created_at and not self.finished_at:
            return tasks

        for task in tasks:

            if self.created_at:
                if self.created_at.from_ and task.created_at < self.created_at.from_:
                    continue
                if self.created_at.to and task.created_at > self.created_at.to:
                    continue

            if self.finished_at:
                if self.finished_at.from_ and (
                        task.finished_at is None or task.finished_at < self.finished_at.from_
                ):
                    continue
                if self.finished_at.to and (
                        task.finished_at is None or task.finished_at > self.finished_at.to
                ):
                    continue

            filtered.append(task)

        return filtered