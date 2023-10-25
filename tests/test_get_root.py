""" 
Script to test GET method on endpoint /
"""
import pytest # W0611, pylint: disable=unused-import
import requests

def test_api_get_root(url = "http://localhost:8085/"):
    """ 
    Test for root endpoint /.

    ...
    Args:
        url: API url.

    Returns:
        None.
    """
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, 'Request failed!'
    response = response.json()
    assert response['info'] == 'nothing here... <address>/docs to documentation', 'Result error!'
