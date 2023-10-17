from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from paddleocr import PaddleOCR
import numpy as np
import cv2

app = FastAPI()

def ocr_process(img):
        ocr = PaddleOCR(use_angle_cls=True)                                                  # need to run only once to download and load the model into memory
        result = ocr.ocr(img, cls=True)
        return result

def read_imagefile(data):
    npimg = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

@app.get("/")
def read_root():
    return {"Image API read!"} 
 
@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    result = ocr_process(image)
    
    return {"result":f"{result}"}

if __name__ == "__main__":
    # uvicorn main:app --reload --host "0.0.0.0" --port 8080
    pass