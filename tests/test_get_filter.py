import pytest
import requests

def test_api_get_filter(url = "http://0.0.0.0:8085/v1/filter/"):
    response = requests.get(url)
    assert response.status_code == 200, "Failed!"
