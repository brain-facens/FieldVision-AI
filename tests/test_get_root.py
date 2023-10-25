import pytest
import requests

def test_api_get_root(url = "http://0.0.0.0:8085"):
    response = requests.get(url)
    assert response.status_code == 200, 'Request failed!'
    response = response.json()
    assert response['info'] == 'nothing here... <address>/docs to documentation', 'Result error!'

if __name__ == '__main__':
    test_api_get_root()