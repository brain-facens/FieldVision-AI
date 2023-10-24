# FieldVision API
API for processing text on invoices, with the aim of identifying relevant fields on an invoice and optimizing bonus or validation systems. Making life easier for logisticians, merchants and managers, the application has an interface that captures images from the webcam, processes the image using OCR and provides a visualization of the results obtained.

Follow the steps bellow to install the FieldVision API:

```
# Clone repository
git clone https://github.com/brain-facens/FieldVision-AI.git

# Install requirements
cd FieldVision-AI/
pip install -r requirements.txt

# Run API
python src/field_vision_API/main.py
```

## API Methods
Below are the methods present in the FieldVision API and their respective functions.

| API Call | Action|
|----------|-------|
| GET / | Home path |
| GET /v1/result/ | Get the filtered result |
| GET /v1/raw_result/ | Get the latest raw result |
| GET /v1/filter/ | Get the latest word filter |
| POST /v1/post_image/ | Upload image |
| PUT /v1/filter/ | Update the filter |




## Example Request Scripts
Below are the scripts that make it possible to request the methods present in the API.

#### **GET** methods:

```
import pytest
import requests

def test_api_call_root(url = <API_url>):
    response = requests.get(url)
    return response
```
---
#### **PUT** methods:

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
   return response
```
---
#### **POST** methods:

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
    return response
```
