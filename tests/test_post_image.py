import base64
import json
import pytest
import requests

def test_api_post_img(url = "http://0.0.0.0:8085/v1/post_image/"):
    img_file = "./docs/demo_image.png"

    payload={}
    files=[
        (
        'file',
        (
            'demo_image', open(img_file,'rb'),
            'image/png'
            )
        )
    ]

    response = requests.post(url, data=payload, files=files)
    assert response.status_code == 200, 'Request failed!'
    response = response.json()
    assert response['result'] == 'result in /raw_result but no filter, please set a filter!', 'Result error!'

if __name__ == '__main__':
    test_api_post_img()