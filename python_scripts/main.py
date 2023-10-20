from utils import (ocr_process, read_imagefile,
                    list_of_strings, Results, Filter)
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import List
import argparse
import uvicorn


app = FastAPI()

parser = argparse.ArgumentParser()
parser.add_argument('--filter', type=list_of_strings, help='the default filter: fist,second,third')
args = parser.parse_args()

filter_words = Filter(args.filter)
results = Results()
raw_results = Results()
class UpdateFilter(BaseModel):
    filter: List[str] = args.filter

@app.get("/")
def read_root():
    return {"info":"nothing here... /docs to documentation"} 

@app.post("/post_image/")
async def post_file(file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    filtered, raw = ocr_process(image, filter_words.get_filter())
    results.set_results(filtered)
    raw_results.set_results(raw)

    return {"result":results.get_results()}

@app.get("/result/")
async def get_latest_result():
    return {"latest_result":results.get_results()}

@app.get("/raw_result/")
async def get_latest_raw_result():
    return {"latest_result":raw_results.get_results()}

@app.put("/filter/")
async def update_flter(filter_: UpdateFilter):
    filter_words.set_filter(filter_.filter)

    return {"new_filter":filter_words.get_filter()}

@app.get("/filter/")
async def get_latest_filter():
    return {"latest_filter":filter_words.get_filter()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
