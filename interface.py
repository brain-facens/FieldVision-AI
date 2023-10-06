import os 
import cv2 as cv
import numpy as np
import streamlit as st
from urllib import request
from paddleocr import PaddleOCR, draw_ocr


class OCR_interface:
    def __init__(self, mode = 0, img_path = '/home/nata-brain/Documents/projects/OCR-notas/data/images/1.jpg', api_uri = 'http://3.147.47.4/show/'):
        self.mode               = mode                              # 0 to capture image from camera, 1 from path and 2 from API
        self.img_file_buffer    = st.camera_input("Tirar foto")
        self.total_value        = {'subtotal': None,
                                   'total': None}
        self.im_show            = None
        self.texts              = None
        self.boxes              = None
        self.font_path          = "fonts/simfang.ttf"                        # Replace this with the path to your preferred TrueType font file.
        self.cv_img             = None
        self.api_uri            = api_uri
        self.img_path           = img_path

    def ocr_process(self):
        ocr = PaddleOCR(use_angle_cls=True)                                                  # need to run only once to download and load the model into memory
        self.result = ocr.ocr(self.cv_img, cls=True)

        for idx in range(len(self.result)):
            res = self.result[idx]
            for line in res:
                print(line)

        # Draw result
        self.result     = self.result[0]
        self.boxes      = [line[0] for line in self.result]  
        self.texts       = [line[1][0] for line in self.result]
        self.scores     = [line[1][1] for line in self.result]
        self.im_show    = draw_ocr(self.cv_img, self.boxes, self.texts, self.scores, font_path = self.font_path)
        
    @staticmethod
    def is_float(value):
        try:
            float_value = float(value)
            return float_value, True
        except:
            return -0.0, False
    
    
    def process_values(self):
        aux = 0
        for i in self.texts:
            if i.upper() == 'SUBTOTAL':
                subtotal, sun_result = self.is_float(self.texts[aux + 1])
                
                if sun_result:
                    self.total_value['subtotal'] = subtotal
                
            if i.upper() == 'TOTAL':
                total, total_result = self.is_float(self.texts[aux + 1])
                
                if total_result:
                    self.total_value['total'] = total
                     
            aux += 1
            
    def pipeline_processing(self) -> None:
        
        if self.mode == 0:
            if self.img_capture():
                self.processing_data()
        elif self.mode == 1:
            self.img_from_url()
            self.processing_data()
        elif self.mode == 2: 
            self.img_from_api(self.api_uri)
            self.processing_data()
        else:
            st.divider()
            st.caption("No Data")     
            return 
                
    def processing_data(self) -> None:    
        self.ocr_process()   
        self.process_values()
        
        st.divider()
        st.caption("Imagem Processada:")
        st.image(cv.cvtColor(self.im_show, cv.COLOR_BGR2RGB))
        st.caption("Dados da Nota:")
        st.table(self.texts)
        st.table(self.total_value)
        
            
    def img_capture(self) -> bool:
        if self.img_file_buffer is not None:
            # To read image file buffer with OpenCV:
            self.cv_img     = cv.imdecode(np.frombuffer(self.img_file_buffer.getvalue(), np.uint8), cv.IMREAD_COLOR)
            return True
        return False

    def img_from_api(self, uri) -> None:
        response = request.urlopen(uri)
        img_array = np.array(bytearray(response.read()), dtype=np.uint8)
        self.cv_img = cv.imdecode(img_array, -1)
        
                
    def img_from_url(self) -> None:
        
        isFile = os.path.isfile(self.img_path)
        
        if isFile:
            self.cv_img     = cv.imread(self.img_path)  
            
     
if __name__ == "__main__":
    interface = OCR_interface(mode=2)
    interface.pipeline_processing()