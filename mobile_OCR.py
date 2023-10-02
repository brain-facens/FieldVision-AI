import cv2
import numpy as np
from paddleocr import PaddleOCR, draw_ocr


class OCRInterface:
    def __init__(self):
        pass

    def ocr_process(self, img, phrases):
        ocr = PaddleOCR(use_angle_cls=True, lang="pt")
        result = ocr.ocr(img, cls=True)

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
                            txts.append(txts_)

        for comp in coord:
            produto = next(iter(comp.keys()))
            coordenada = comp[produto]

            xy_min = coordenada[0]
            xy_max = coordenada[2]

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
                        text_lines_sec.append(axis[1][0])
                        boxes_sec.append(axis[0])

        num_boxes = len(boxes)
        boxes = np.array(boxes).reshape(num_boxes, 4, 2).astype(np.int64)

        num_boxes_sec = len(boxes_sec)
        boxes_sec = np.array(boxes_sec).reshape(num_boxes_sec, 4, 2).astype(np.int64)

        all_boxes = np.concatenate((boxes, boxes_sec), axis=0)
        all_texts = np.concatenate((text_lines, text_lines_sec), axis=0)
        print(all_texts)
        return all_texts  # Apenas retornar a lista de textos


if __name__ == "__main__":
    interface = OCRInterface()
