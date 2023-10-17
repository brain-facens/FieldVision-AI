from fastapi import FastAPI, File, UploadFile
from utils import ocr_process, read_imagefile

app = FastAPI()

@app.get("/")
def read_root():
    return {"Image API read!"} 

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    phrases = ["RUA", "TOTAL", "CNPJ"]
    img_result, txt = ocr_process(image, phrases)
    print(txt)
    return {"result":f"{txt}"}


if __name__ == "__main__":
    # uvicorn main:app --reload --host "0.0.0.0" --port 8080
    pass