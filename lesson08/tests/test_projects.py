import pytest
import requests


class TestProjectsAPI:

    @pytest.mark.positive
    def test_create_project_success(self, yougile_api, unique_name):
        response = yougile_api.create_project(
            title=unique_name,
            description="Test project description"
        )

        assert response["status_code"] == 201
        assert "id" in response["data"]
        assert response["data"]["title"] == unique_name
        assert response["data"]["description"] == "Test project description"

    @pytest.mark.positive
    def test_get_project_success(self, yougile_api, created_project):
        response = yougile_api.get_project(created_project)

        assert response["status_code"] == 200
        assert response["data"]["id"] == created_project
        assert "title" in response["data"]
        assert "description" in response["data"]

    @pytest.mark.positive
    def test_update_project_success(self, yougile_api, created_project, unique_name):
        new_title = f"updated_{unique_name}"
        new_description = "Updated description"

        response = yougile_api.update_project(
            project_id=created_project,
            title=new_title,
            description=new_description
        )

        assert response["status_code"] == 200
        assert response["data"]["title"] == new_title
        assert response["data"]["description"] == new_description

        get_response = yougile_api.get_project(created_project)
        assert get_response["data"]["title"] == new_title

    @pytest.mark.negative
    def test_create_project_without_title(self, yougile_api):
        response = yougile_api.create_project(title="")

        assert response["status_code"] in [400, 422]

    @pytest.mark.negative
    def test_get_nonexistent_project(self, yougile_api):
        nonexistent_id = "nonexistent_project_id_12345"
        response = yougile_api.get_project(nonexistent_id)

        assert response["status_code"] == 404

    @pytest.mark.negative
    def test_update_nonexistent_project(self, yougile_api, unique_name):
        nonexistent_id = "nonexistent_project_id_12345"

        response = yougile_api.update_project(
            project_id=nonexistent_id,
            title=unique_name
        )

        assert response["status_code"] == 404

    @pytest.mark.negative
    def test_update_project_empty_data(self, yougile_api, created_project):
        response = yougile_api.update_project(project_id=created_project)

        assert response["status_code"] in [200, 400]

    @pytest.mark.negative
    def test_create_project_with_invalid_auth(self, base_url, unique_name):
        invalid_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer invalid_api_key_12345"
        }

        data = {
            "title": unique_name,
            "description": "Test project"
        }

        response = requests.post(
            f"{base_url}/projects",
            json=data,
            headers=invalid_headers
        )

        assert response.status_code in [401, 403]


@pytest.fixture
def yougile_api(base_url, api_key):
    from api.yougile_api import YouGileAPI
    return YouGileAPI(base_url, api_key)
