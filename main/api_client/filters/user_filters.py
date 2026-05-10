from typing import Optional, List
from pydantic import BaseModel

from main.api_client.schemas.place import Place


class UserFilterSet(BaseModel):

    ids: Optional[List[int]] = None
    permission_groups: Optional[List[str]] = None

    def __eq__(self, other):
        if not isinstance(other, UserFilterSet):
            return False
        return self.ids == other.ids and self.permission_groups == other.permission_groups

    def build_query_params(self) -> dict:

        params = {}

        if self.ids:
            params["u:ids[]"] = self.ids
        if self.permission_groups:
            params["u:permission_groups[]"] = self.permission_groups

        return params


