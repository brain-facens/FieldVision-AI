import pytest
import requests

def test_api_get_result(url = "http://0.0.0.0:8085/v1/result/"):
    response = requests.get(url)
    assert response.status_code == 200, "Failed!"
    response = response.json()
    assert type(response['latest_result']) == list, 'Result error!'

if __name__ == '__main__':
    test_api_get_result()