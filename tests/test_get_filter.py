import pytest
import requests

def test_api_get_filter(url = "http://0.0.0.0:8085/v1/filter/"):
    response = requests.get(url)
    assert response.status_code == 200, "Failed!"
    response = response.json()
    assert response['latest_filter'] == None, 'Result error!'
 
if __name__ == '__main__':
    test_api_get_filter()