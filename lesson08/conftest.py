import pytest
import requests
import uuid
import os


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "positive: позитивные тесты"
    )
    config.addinivalue_line(
        "markers", "negative: негативные тесты"
    )


@pytest.fixture(scope="session")
def base_url():
    return "https://yougile.com/api-v2"


@pytest.fixture(scope="session")
def api_key():
    key = os.getenv("YOUGILE_API_KEY")
    if not key:
        pytest.fail("YOUGILE_API_KEY environment variable not set")
    return key


@pytest.fixture(scope="session")
def headers(api_key):
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }


@pytest.fixture
def unique_name():
    return f"test_project_{uuid.uuid4().hex[:8]}"


@pytest.fixture
def created_project(base_url, headers, unique_name):
    project_data = {
        "title": unique_name,
        "description": "Test project for automated testing"
    }

    response = requests.post(
        f"{base_url}/projects",
        json=project_data,
        headers=headers
    )

    if response.status_code != 201:
        pytest.fail(f"Failed to create test project: {response.text}")

    project_id = response.json()["id"]

    yield project_id

    requests.delete(f"{base_url}/projects/{project_id}", headers=headers)
