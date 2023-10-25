""" 
Script to test GET method endpoint /v1/raw_result/.
"""
import pytest # W0611, pylint: disable=unused-import
import requests

def test_api_get_raw_result(url = "http://localhost:8085/v1/raw_result/"):
    """ 
    Test for endpoint raw result /v1/raw_result/.

    ...
    Args:
        url: API url.

    Returns:
        None.
    """
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, "Failed!"
    response = response.json()
    assert isinstance(response['latest_result'], list), 'Result error!'
