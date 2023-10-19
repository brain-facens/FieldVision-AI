from paddleocr import PaddleOCR
import numpy as np
import cv2


def read_imagefile(data):
    npimg = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

def ocr_process(img, phrases):
        ocr = PaddleOCR(use_angle_cls=True, lang="pt", show_log=False)  # Initialize PaddleOCR
        result = ocr.ocr(img, cls=True)  # Get OCR results for the input image

        # Extract relevant information from OCR results based on specified phrases
        coord = []
        text_lines = []
        text_lines_sec = []
        boxes = []
        boxes_sec = []
        txts = []

        for f in phrases:
            phrase = f.upper().replace(" ", "").replace("$","S")

            for idx in result:
                for line in idx:
                    _line_plus = line[1][0].upper().replace(" ", "").replace("$","S")
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

        all_texts = np.concatenate((text_lines, text_lines_sec), axis=0)

        return all_texts
