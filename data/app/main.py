from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr
from typing import Union
import os

# path to save uploaded images
IMAGEDIR = "../images/"
 
app = FastAPI()

class ReportBase(BaseModel):
    ocr_data: str
    

# root API path
@app.get("/")
def read_root():
    return {"Image API read!"} 
 
# upload image service 
@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
 
    file.filename = f"1.jpg"
    contents = await file.read()
 
    #save the file 
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
 
    return {"filename": file.filename}


# upload text data service 
@app.post("/report/")
async def create_upload_data(report: ReportBase):
    return report
 
# get image  
@app.get("/show/")
async def read_random_file():
 
    # get random file from the image directory
    files = os.listdir(IMAGEDIR)
    random_index = 0
 
    path = f"{IMAGEDIR}{files[random_index]}"
     
    return FileResponse(path)
