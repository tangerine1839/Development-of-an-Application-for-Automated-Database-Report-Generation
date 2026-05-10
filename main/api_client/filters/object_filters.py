from typing import Optional, List
from pydantic import BaseModel

from main.api_client.schemas.place import Place


class ObjectFilterSet(BaseModel):

    codes: Optional[List[str]] = None
    manager: Optional[List[str]] = None

    def __eq__(self, other):
        if not isinstance(other, ObjectFilterSet):
            return False
        return self.codes == other.codes

    def __repr__(self):
        return f"ObjectFilterSet(codes={self.codes})"

    def filter_python(
            self,
            places: List[Place],
    ) -> List[Place]:

        filtered = []
        if not self.manager:
            return places

        for place in places:
            if place.manager and place.manager in self.manager:
                filtered.append(place)

        return filtered
    def build_query_params(self) -> dict:

        params = {}

        if self.codes:
            params["s:codes[]"] = self.codes

        return params


