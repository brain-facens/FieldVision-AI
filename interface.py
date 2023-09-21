import cv2 as cv
import numpy as np
import streamlit as st
import urllib.request as request
from paddleocr import PaddleOCR, draw_ocr


class OCR_interface:
    def __init__(self):
        self.img_file_buffer    = st.camera_input("Tirar foto")
        self.total_value        = {'subtotal': None,
                                   'total': None}
        self.im_show            = None
        self.txts               = None
        self.boxes              = None
        self.font_path          = "/root/OCR-notas/fonts/simfang.ttf"                        # Replace this with the path to your preferred TrueType font file.
        self.cv_img            = None

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
        self.txts       = [line[1][0] for line in self.result]
        self.scores     = [line[1][1] for line in self.result]
        self.im_show    = draw_ocr(self.cv_img, self.boxes, self.txts, self.scores, font_path = self.font_path)
        
    @staticmethod
    def is_float(value):
        try:
            float_value = float(value)
            return float_value, True
        except:
            return -0.0, False
    
    
    def process_values(self):
        aux = 0
        for i in self.txts:
            if i.upper() == 'SUBTOTAL':
                subtotal, sun_result = self.is_float(self.txts[aux + 1])
                
                if sun_result:
                    self.total_value['subtotal'] = subtotal
                
            if i.upper() == 'TOTAL':
                total, total_result = self.is_float(self.txts[aux + 1])
                
                if total_result:
                    self.total_value['total'] = total
                     
            aux += 1
        

    def img_capture(self):
        if self.img_file_buffer is not None:

            # To read image file buffer with OpenCV:
            self.cv_img     = cv.imdecode(np.frombuffer(self.img_file_buffer.getvalue(), np.uint8), cv.IMREAD_COLOR)
            self.ocr_process()   
            self.process_values()
            
            st.divider()
            st.caption("Imagem Processada:")
            st.image(cv.cvtColor(self.im_show, cv.COLOR_BGR2RGB))
            st.caption("Dados da Nota:")
            st.table(self.txts)
            st.table(self.total_value)

            
    def img_from_url(self):
        url_response = request.urlopen('https://web-dev.imgix.net/image/tcFciHGuF3MxnTr1y5ue01OGLBn2/egsW6tkKWYI8IHE6JyMZ.png?auto=format&w=439')
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv.imdecode(img_array, -1)
        self.cv_img     = img
        self.ocr_process()   
        self.process_values()
        
        st.divider()
        st.caption("Imagem Processada:")
        st.image(cv.cvtColor(self.im_show, cv.COLOR_BGR2RGB))
        st.caption("Dados da Nota:")
        st.table(self.txts)
        st.table(self.total_value)       
            
            
if __name__ == "__main__":
    interface = OCR_interface()
    interface.img_capture()