from typing import Optional, List

import httpx

from main.api_client.filters.inspection_filters import InspectionFilterSet
from main.api_client.filters.object_filters import ObjectFilterSet
from main.api_client.filters.task_filters import TaskFilterSet
from main.api_client.filters.user_filters import UserFilterSet
from main.api_client.responses.inspection_items import InspectionItemsResponse
from main.api_client.responses.task_list import TaskListResponse
from main.api_client.responses.object_list import ObjectListResponse
from main.api_client.responses.task_messages import TaskMessagesResponse
from main.api_client.responses.users_list import UserListResponse
from main.api_client.schemas.inspection_short import InspectionShort
from main.api_client.schemas.task_short import TaskShort
from main.api_client.schemas.user import User
from main.config import settings
from main.api_client.schemas.place import Place
from main.api_client.responses.inspections_list import InspectionListResponse


class CheckOfficeAPIClient:
    def __init__(self, api_key: str, base_url: str):
        self.base_url = base_url.rstrip("/")
        self._http = httpx.Client(
            headers={
                "accept": "application/json",
                "API-Key": api_key,
            },
            timeout=30.0,
        )


    def get_users(
            self,
            page: int = 1,
            per_page: int = 30,
            filters: Optional[UserFilterSet] = None,
    ) -> UserListResponse:

        url = f"{self.base_url}/publicapi/v1/users"
        params = {
            "page": page,
            "per_page": per_page,
        }

        if filters:
            params.update(filters.build_query_params())

        response = self._http.get(url, params=params)
        response.raise_for_status()
        raw = response.json()
        return UserListResponse.model_validate(raw)


    def get_all_users(
            self,
            filters: Optional[UserFilterSet] = None,
    ) -> List[User]:

        resp = self.get_users(page=1, per_page=30, filters=filters)
        total_pages = resp.last_page
        all_users: List[User] = []

        for page in range(1, total_pages + 1):
            page_resp = self.get_users(page=page, per_page=30, filters=filters)
            all_users.extend(page_resp.data)

        return all_users

    def get_inspection_by_id(self, inspection_id: int) -> InspectionItemsResponse:

        url = f"{self.base_url}/publicapi/v1/inspections/{inspection_id}"
        response = self._http.get(url)
        response.raise_for_status()
        raw = response.json()

        return InspectionItemsResponse.model_validate(raw)


    def get_task_by_id(self, task_id: int) -> TaskMessagesResponse:

        url = f"{self.base_url}/publicapi/v1/tasks/{task_id}"
        response = self._http.get(url)
        response.raise_for_status()
        raw = response.json()

        return TaskMessagesResponse.model_validate(raw)


    def get_inspections(
            self,
            page: int = 1,
            per_page: int = 30,
            filters: Optional[InspectionFilterSet] = None,
    ) -> InspectionListResponse:

        url = f"{self.base_url}/publicapi/v1/inspections"
        params = {
            "page": page,
            "per_page": per_page,
        }

        if filters:
            params.update(filters.build_query_params())
        response = self._http.get(url, params=params)
        response.raise_for_status()
        raw = response.json()
        return InspectionListResponse.model_validate(raw)


    def get_all_inspections(
            self,
            filters: Optional[InspectionFilterSet] = None,
    ) -> List[InspectionShort]:

        resp = self.get_inspections(page=1, per_page=30, filters=filters)
        total_pages = resp.last_page

        all_tasks: List[InspectionShort] = []

        for page in range(1, total_pages + 1):
            page_resp = self.get_inspections(page=page, per_page=30, filters=filters)
            all_tasks.extend(page_resp.data)

        return all_tasks

    def get_objects(
            self,
            page: int = 1,
            per_page: int = 30,
            filters: Optional[ObjectFilterSet] = None,
    ) -> ObjectListResponse:

        url = f"{self.base_url}/publicapi/v1/places"
        params = {
            "page": page,
            "per_page": per_page,
        }

        if filters:
            params.update(filters.build_query_params())
        response = self._http.get(url, params=params)
        response.raise_for_status()
        raw = response.json()
        return ObjectListResponse.model_validate(raw)

    def get_all_objects(
            self,
            filters: Optional[ObjectFilterSet] = None,
    ) -> List[Place]:

        resp = self.get_objects(page=1, per_page=30, filters=filters)
        total_pages = resp.data.last_page

        all_objects: List[Place] = []

        for page in range(1, total_pages + 1):
            page_resp = self.get_objects(page=page, per_page=30, filters=filters)
            all_objects.extend(page_resp.data.data)

        return all_objects

    def get_tasks(
            self,
            page: int = 1,
            per_page: int = 30,
            filters: Optional[TaskFilterSet] = None,
    ) -> TaskListResponse:

        url = f"{self.base_url}/publicapi/v1/tasks"
        params = {
            "page": page,
            "per_page": per_page,
        }

        if filters:
            params.update(filters.build_query_params())
        response = self._http.get(url, params=params)
        response.raise_for_status()
        raw = response.json()
        return TaskListResponse.model_validate(raw)


    def get_all_tasks(
            self,
            filters: Optional[TaskFilterSet] = None,
    ) -> List[TaskShort]:

        resp = self.get_tasks(page=1, per_page=30, filters=filters)
        total_pages = resp.last_page

        all_tasks: List[TaskShort] = []

        for page in range(1, total_pages + 1):
            page_resp = self.get_tasks(page=page, per_page=30, filters=filters)
            all_tasks.extend(page_resp.data)

        return all_tasks

    def close(self):
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()