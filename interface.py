import streamlit as st
import re
import cv2
import numpy as np
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class OCR_interface:
    def __init__(self):
        self.img_file_buffer = st.camera_input("Tirar foto")

    def ocr_process(self, img = None):
        
        ocr = PaddleOCR(use_angle_cls=True)  # need to run only once to download and load the model into memory
        img_path = img
        result = ocr.ocr(img_path, cls=True)

        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line)

        # Draw result
        result = result[0]
        image = img #Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]  
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        font_path = "/root/OCR-notas/fonts/simfang.ttf"  # Replace this with the path to your preferred TrueType font file.
        im_show = draw_ocr(image, boxes, txts, scores, font_path=font_path)
        
        return im_show, txts
    
    def is_float(self, value):
        try:
            float_value = float(value)
            return float_value, True
        except:
            return -0.0, False
    
    def process_values(self, strInfo):
        
        """ 
        numeric_pattern = r"[\d,]+(?:\.\d+)?"
        numeric_values = re.findall(numeric_pattern, strInfo)
        numeric_values = [float(value.replace(",", "")) for value in numeric_values]
        
        X = np.arange(len(numeric_values)).reshape(-1, 1)
        y = np.array(numeric_values).reshape(-1, 1)
        
        
        model = LinearRegression()
        model.fit(X, y)
        
        total_price = model.predict([[len(numeric_values) - 1]])[0][0]

        print(f"Total Price: ${total_price:.2f}") """
        total_value = {'subtotal': None,
                       'total': None}
        
        aux = 0
        for i in strInfo:
            if i.upper() == 'SUBTOTAL':
                subtotal, sun_result = self.is_float(strInfo[aux + 1])
                
                if sun_result:
                    total_value['subtotal'] = subtotal
                
            if i.upper() == 'TOTAL':
                total, total_result = self.is_float(strInfo[aux + 1])
                
                if total_result:
                    total_value['total'] = total
                    
                    
            aux += 1
        
        return total_value
        

    def img_capture(self):
        if self.img_file_buffer is not None:
            # To read image file buffer with OpenCV:
            bytes_data  = self.img_file_buffer.getvalue()
            cv2_img     = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            img_result, txt  = self.ocr_process(cv2_img)
                        
            total_value = self.process_values(txt)
            
            #cv2.imwrite("image_processed.png", img_result)
            st.divider()
            st.caption("Imagem Processada:")
            st.image(cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB))
            st.caption("Dados da Nota:")
            st.table(txt)
            st.table(total_value)
            
if __name__ == "__main__":
    interface = OCR_interface()
    interface.img_capture()