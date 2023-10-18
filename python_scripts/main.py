from fastapi import FastAPI, File, UploadFile
from utils import ocr_process, read_imagefile
import argparse
import uvicorn

parser = argparse.ArgumentParser()

app = FastAPI()

def list_of_strings(arg):
    return arg.split(',')

parser.add_argument('--phrases', type=list_of_strings)

args = parser.parse_args()
print(args.phrases)

@app.get("/")
def read_root():
    return {"Image API read!"} 

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    phrases = args.phrases
    img_result, txt = ocr_process(image, phrases)
    return {"result":f"{txt}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)