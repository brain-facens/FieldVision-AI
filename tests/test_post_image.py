""" 
Script to test POST method on endpoint /v1/post_image/
"""
import pytest # W0611, pylint: disable=unused-import
import requests

def test_api_post_img(url = "http://localhost:8085/v1/post_image/"):
    """ 
    Test for endpoint /v1/post_image/.

    ...
    Args:
        url: API url.

    Returns:
        None.
    """
    contents = ''
    img_file = "./docs/demo_image.png"
    expected_result = 'result in /raw_result but no filter, please set a filter!'

    with open(img_file, "rb") as file:
        contents = file.read()

    payload={}
    files=[
        (
        'file',
        (
            'demo_image', contents,
            'image/png'
            )
        )
    ]

    response = requests.post(url, data=payload, files=files, timeout=10)
    assert response.status_code == 200, 'Request failed!'
    response = response.json()
    assert response['result'] == expected_result, 'Result error!'
