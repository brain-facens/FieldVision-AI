import os
import cv2 as cv
import numpy as np
import streamlit as st
from urllib import request
from paddleocr import PaddleOCR, draw_ocr


class OCR_interface:
    def __init__(
        self,
        phrases,
        img_path="/home/pedro/Documents/OCR-notas/data/images/1.jpg",
        api_uri="http://18.220.184.248/show/",
    ):
        self.txts = None
        self.boxes = None
        self.cv_img = None
        self.im_show = None
        self.api_uri = api_uri
        self.phrases = phrases
        self.img_path = img_path
        self.font_path = "/home/pedro/Documents/OCR-notas/fonts/simfang.ttf"  # Replace this with the path to your preferred TrueType font file.

    # def ocr_process(self):
    #     ocr = PaddleOCR(use_angle_cls=True)                                                  # need to run only once to download and load the model into memory
    #     self.result = ocr.ocr(self.cv_img, cls=True)

    #     for idx in range(len(self.result)):
    #         res = self.result[idx]
    #         for line in res:
    #             print(line)

    #     # Draw result
    #     self.result     = self.result[0]
    #     self.boxes      = [line[0] for line in self.result]
    #     self.texts       = [line[1][0] for line in self.result]
    #     self.scores     = [line[1][1] for line in self.result]
    #     self.im_show    = draw_ocr(self.cv_img, self.boxes, self.texts, self.scores, font_path = self.font_path)

    def ocr_process(self):
        ocr = PaddleOCR(use_angle_cls=True, lang="pt")  # Initialize PaddleOCR
        img = self.cv_img
        phrases = self.phrases
        result = ocr.ocr(img, cls=True)  # Get OCR results for the input image

        # Extract relevant information from OCR results based on specified phrases
        coord = []
        text_lines = []
        text_lines_sec = []
        boxes = []
        boxes_sec = []
        txts = []

        for f in phrases:
            phrase = f.upper().replace(" ", "").replace("$", "S")

            for idx in result:
                for line in idx:
                    _line_plus = line[1][0].upper().replace(" ", "").replace("$", "S")
                    line_plus = _line_plus[: len(phrase)]

                    if line_plus == phrase:
                        coord.append({line[1][0]: line[0]})
                        text_lines.append(line[1][0])
                        boxes.append(line[0])

                        if len(phrase) != len(_line_plus):
                            txts_ = line[1][0]
                            txts_ = txts_.split(f)
                            print(f"{f}:{txts_[1]}")
                            txts.append(txts_)

        # Process the found coordinates
        for comp in coord:
            produto = next(iter(comp.keys()))
            coordenada = comp[produto]

            xy_min = coordenada[0]
            xy_max = coordenada[2]

            print(f"\n\nCOORDENADA DO CAMPO ({produto}) {xy_min, xy_max}\n")
            for l in result:
                for axis in l:
                    _xy_min = axis[0][0]
                    _xy_max = axis[0][2]

                    compara_min = xy_min[1] / _xy_min[1]
                    compara_max = xy_max[1] / _xy_max[1]

                    diferente = False
                    if (
                        xy_min[0] != _xy_min[0]
                        and xy_max[0] != _xy_max[0]
                        and xy_min[0] < _xy_min[0]
                        and xy_max[0] < _xy_max[0]
                    ):
                        diferente = True

                    if (
                        (compara_min >= 0.98 and compara_min <= 1.02)
                        and (compara_max >= 0.98 and compara_max <= 1.02)
                        and (diferente == True)
                        and (axis[0] not in boxes)
                    ):
                        print(
                            f"ACHOU, CAMPO ({axis[1][0]}), Coordenada {_xy_min, _xy_max}"
                        )
                        text_lines_sec.append(axis[1][0])
                        boxes_sec.append(axis[0])

        num_boxes = len(boxes)
        boxes = np.array(boxes).reshape(num_boxes, 4, 2).astype(np.int64)

        num_boxes_sec = len(boxes_sec)
        boxes_sec = np.array(boxes_sec).reshape(num_boxes_sec, 4, 2).astype(np.int64)

        self.boxes = np.concatenate((boxes, boxes_sec), axis=0)
        self.txts = np.concatenate((text_lines, text_lines_sec), axis=0)

        self.result = result[0]
        image = img
        # self.im_show = draw_ocr(image, self.boxes, self.txts, self.font_path)

    @staticmethod
    def is_float(value):
        try:
            float_value = float(value)
            return float_value, True
        except:
            return -0.0, False

    def processing_data(self) -> None:
        response = request.urlopen(self.api_uri)
        img_array = np.array(bytearray(response.read()), dtype=np.uint8)
        self.cv_img = cv.imdecode(img_array, -1)

        self.ocr_process()

        st.divider()
        st.caption("Imagem Processada:")
        # st.image(cv.cvtColor(self.im_show, cv.COLOR_BGR2RGB))
        st.caption("Dados da Nota:")
        st.table(self.txts)


if __name__ == "__main__":
    interface = OCR_interface(phrases=["RUA", "TOTAL", "CNPJ"])
    interface.processing_data()
