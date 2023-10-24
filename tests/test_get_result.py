import pytest
import requests

def test_api_get_result(url = "http://0.0.0.0:8085/v1/result/"):
    response = requests.get(url)
    assert response.status_code == 200, "Failed!"
