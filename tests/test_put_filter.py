import pytest
import requests

def test_api_put_result(url = "http://0.0.0.0:8085/v1/filter/"):
    payload={
        "filter": [
            "total"
        ]
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200, "Failed!"
