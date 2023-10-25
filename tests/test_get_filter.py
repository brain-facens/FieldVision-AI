""" 
Script to test GET method endpoint /v1/filter/.
"""

import pytest # W0611, pylint: disable=unused-import
import requests

def test_api_get_filter(url = "http://localhost:8085/v1/filter/") -> None:
    """ 
    Test for endpoint filter result /v1/filter/.

    ...
    Args:
        url: API url.

    Returns:
        None.
    """
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, "Failed!\n"
    response = response.json()
    assert response['latest_filter'] is None, 'Result error!\n'
