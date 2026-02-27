import os
import requests


def test_api_authentication():
    api_key = os.getenv("YOUGILE_API_KEY")
    if not api_key:
        return False

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(
            "https://yougile.com/api-v2/projects",
            headers=headers
        )

        if response.status_code == 200:
            projects = response.json()
            for project in projects[:3]:
                title = project.get('title', 'No title')
                project_id = project.get('id', 'No ID')
                print(f"{title} (ID: {project_id})")
            return True
        elif response.status_code == 401:
            return False
        elif response.status_code == 403:
            return False
        else:
            return False

    except Exception:
        return False


if __name__ == "__main__":
    test_api_authentication()
