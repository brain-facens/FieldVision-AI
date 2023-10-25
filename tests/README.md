## Test Cases for API Testing
To test the API, some test cases were created, which are shown in the table below.

| Test Scenario Category | Test Action Category | Test Action Description |
|------------------------|----------------------|-------------------------|
| ***1 Basic Positive Tests*** |||
| Execute API call with valid required parameters| Validate status code:| 1. All requests should return 2XX HTTP status code <br> 2. Returned status code is according to spec: <br> - 200 OK for **GET**, **POST** and **PUT** request <br> 3. Validate returns with expected API data: <br> - **GET** /, returns: Information for user to found the API docs <br> - **GET** /v1/result/, returns: Information for user to found the API docs <br> - **GET** /v1/raw_result/, returns: Latest OCR processing raw result <br> - **GET** /v1/filter/, returns the latest word filter on API <br> - **POST** /v1/post_image/, returns: Information for user to found the API docs <br> - **PUT** /v1/filter/, returns: The new filter |

To run the tests, the API must be running. After checking this, run the commands below:
```
# Go to the repository's root folder
cd FieldVision-AI

# Run pytest
pytest
```
---

## Example Test scripts

How to test **GET** methods:

```
import pytest
import requests

def test_api_call_root(url = <API_url>):
    response = requests.get(url)
    assert response.status_code == 200, "Failed!"
```
---
How to test **PUT** methods:

```
import pytest
import requests

def test_api_put_result(url = <API_url>):
    payload={
        "filter": [
            "total"
        ]
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200, "Failed!"
```
---
How to test **POST** methods:

```
import pytest
import requests

def test_api_put_result(url = <API_url>):
    payload={
        "filter": [
            "total"
        ]
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200, "Failed!"
```
