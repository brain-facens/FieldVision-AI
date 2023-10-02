import cv2 as cv
import numpy as np
from urllib import request

def img_from_api(uri):
    response = request.urlopen(uri)
    img_array = np.array(bytearray(response.read()), dtype=np.uint8)
    img = cv.imdecode(img_array, -1)
    
       
    return img


# change uri here to others API
if __name__ == '__main__':
    response = img_from_api('http://127.0.0.1:8000/show/')
    print(response.shape)
