import requests


def test_status_code(base_url, status_code):
    current_status_code = requests.get(base_url, allow_redirects=False).status_code
    assert status_code == str(current_status_code)