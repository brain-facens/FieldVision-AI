""" 
Script to test PUT method on endpoint /v1/filter/
"""
import pytest # W0611, pylint: disable=unused-import
import requests

def test_api_put_result(url = "http://0.0.0.0:8085/v1/filter/"):
    """ 
    Test for endpoint /v1/filter/.

    ...
    Args:
        url: API url.

    Returns:
        None.
    """
    payload={
        "filter": [
            "total"
        ]
    }

    response = requests.put(url, json=payload, timeout=10)
    assert response.status_code == 200, "Failed!"
