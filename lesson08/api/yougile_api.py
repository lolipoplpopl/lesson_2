import requests
from typing import Dict, Any


class YouGileAPI:

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def create_project(self, title: str, description: str = "") -> Dict[str, Any]:
        data = {
            "title": title,
            "description": description
        }

        response = requests.post(
            f"{self.base_url}/projects",
            json=data,
            headers=self.headers
        )

        return {
            "status_code": response.status_code,
            "data": response.json() if response.content else {},
            "headers": response.headers
        }

    def get_project(self, project_id: str) -> Dict[str, Any]:
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )

        return {
            "status_code": response.status_code,
            "data": response.json() if response.content else {},
            "headers": response.headers
        }

    def update_project(self, project_id: str, **kwargs) -> Dict[str, Any]:
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=kwargs,
            headers=self.headers
        )

        return {
            "status_code": response.status_code,
            "data": response.json() if response.content else {},
            "headers": response.headers
        }
