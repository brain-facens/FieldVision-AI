from fastapi import FastAPI, File, UploadFile
from utils import ocr_process, read_imagefile
from pydantic import BaseModel
from typing import List
import argparse
import uvicorn


class Filter:
    def __init__(self, filter_:List[str]):
        self._filter_words = filter_

    def set_filter(self, new_filter):
        self._filter_words = new_filter

    def get_filter(self):
        return self._filter_words
    
class Results:
    def __init__(self):
        self._results = []

    def set_results(self, new_results):
        self._results = new_results

    def get_results(self):
        return self._results
    
results = Results()

parser = argparse.ArgumentParser()

app = FastAPI()

def list_of_strings(arg):
    return arg.split(',')

parser.add_argument('--filter', type=list_of_strings, help='the default filter: fist,second,third')

args = parser.parse_args()
filter_words = Filter(args.filter)
class UpdateFilter(BaseModel):
    filter: List[str] = args.filter

@app.get("/")
def read_root():
    return {"info":"nothing here... /docs to documentation"} 

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    print(type(filter_words.get_filter()),filter_words.get_filter())
    results.set_results(ocr_process(image, filter_words.get_filter()))

    return {"result":results.get_results()}

@app.get("/upload/")
async def get_latest_result():
    return {"latest_result":results.get_results()}

@app.put("/filter/")
async def update_flter(filter_: UpdateFilter):
    filter_words.set_filter(filter_.filter)

    return {"new_filter":filter_words.get_filter()}

@app.get("/filter/")
async def get_latest_filter():
    return {"latest_filter":filter_words.get_filter()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
