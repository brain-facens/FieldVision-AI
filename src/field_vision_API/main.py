""" 
Developed by: BRAIN - Brazilian Artificial Inteligence Nucleus
--------------------------------------------------------------
Developers: Natanael Vitorino, Lucas Oliveira and Pedro Santos
---
e-mail: natanael.vitorino@facens.br, lucas.camargo@facens.br 
        and pedro.santos@facens.br
---        
BRAIN, Sorocaba, Brazil, 2023
--------------------------------------------------------------
Description: A system for processing text on invoices, with 
the aim of identifying relevant fields on an invoice and 
optimizing rebate or validation systems. Making life easier 
for logistics operators, merchants and managers, the 
application has an interface that captures webcam images, 
processes the image using OCR and makes it possible to view 
the results obtained.
...
API
"""
from typing import List
import argparse
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel # E0611, pylint: disable=no-name-in-module
import uvicorn
from util.utils import (ocr_process, filter_process, read_imagefile,
                    list_of_strings, Results, Filter)


app = FastAPI()

parser = argparse.ArgumentParser()
parser.add_argument('--filter', type=list_of_strings, help='the default filter: fist,second,third')
args = parser.parse_args()

filter_words = Filter(args.filter)
results = Results()

raw_results = Results()
class UpdateFilter(BaseModel): # R0903, pylint: disable=too-few-public-methods
    """
    Model for structuring the input word that will be the filter.

    ...
    
    Attributes
    ----------
    BaseModel : data model
        Word to filter.

    Methods
    -------
    """
    filter: List[str] = args.filter

@app.get("/")
def read_root():
    """ 
    GET method for API root/home path.

    Args:

    Returns:
        Information for user to found the API docs.
    """
    return {"info":"nothing here... <address>/docs to documentation"}

@app.post("/v1/post_image/")
async def post_file(file: UploadFile = File(...)):
    """ 
    POST method to upload image.

    Args:

    Returns:
        Information for user to found the API docs.
    """

    image = read_imagefile(await file.read())
    raw = ocr_process(image)
    raw_results.set_results(raw)

    if filter_words.get_filter() is None:
        return {"result":"result in /raw_result but no filter, please set a filter!"}

    filtered = filter_process(image, filter_words.get_filter())
    results.set_results(filtered)

    return {"result":results.get_results()}

@app.get("/v1/result/")
async def get_latest_result():
    """ 
    GET method to get the latest result.

    Args:

    Returns:
        Latest OCR processing result.
    """

    return {"latest_result":results.get_results()}

@app.get("/v1/raw_result/")
async def get_latest_raw_result():
    """ 
    GET method to get the latest raw result.

    Args:

    Returns:
        Latest OCR processing raw result.
    """
    return {"latest_result":raw_results.get_results()}

@app.put("/v1/filter/")
async def update_filter(filter_: UpdateFilter):
    """ 
    PUT method to update the filter.

    Args:
        filter_: structural model of the input of 
        the new filter entered by the user.

    Returns:
        The new filter.
    """

    filter_words.set_filter(filter_.filter)

    return {"new_filter":filter_words.get_filter()}

@app.get("/v1/filter/")
async def get_latest_filter():
    """ 
    GET method to get the latest filter on API.

    Args:

    Returns:
        Returns the latest word filter on API.
    """

    return {"latest_filter":filter_words.get_filter()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)
