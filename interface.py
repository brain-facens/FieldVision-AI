import streamlit as st
import cv2
import numpy as np
from paddleocr import PaddleOCR, draw_ocr

class OCR_interface:
    def __init__(self):
        self.img_file_buffer = st.camera_input("Tirar foto")

    # Processing the IMG with PaddleOCR
    def ocr_process(self, img = None):
        
        ocr         = PaddleOCR(use_angle_cls=True, lang = 'pt')                    # Need to run only once to download and load the model into memory
        img_path    = img
        result      = ocr.ocr(img_path, cls=True)                                   # Get infos from image

        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line)

        result      = result[0]
        image       = img                                                           # If you want to process a file, please use: Image.open(img_path).convert('RGB')
        boxes       = [line[0] for line in result]  
        txts        = [line[1][0] for line in result]
        scores      = [line[1][1] for line in result]
        font_path   = "/root/OCR-notas/fonts/simfang.ttf"                           # Replace this with the path to your preferred TrueType font file.
        im_show     = draw_ocr(image, boxes, txts, scores, font_path=font_path)     # Draw result
        
        return im_show, txts

    # To get image from streamlit interface
    def img_capture(self):
        if self.img_file_buffer is not None:
            bytes_data          = self.img_file_buffer.getvalue()                                       # To read image file buffer with OpenCV
            cv2_img             = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            img_result, txt     = self.ocr_process(cv2_img)                                             # To get the infos processed from image
            
            st.divider()
            st.caption("Imagem Processada:")
            st.image(cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB))                                       # To show image in the interface
            st.caption("Dados da Nota:")
            st.table(txt)                                                                               # To show text results 
            
if __name__ == "__main__":
    interface = OCR_interface()
    interface.img_capture()