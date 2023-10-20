from paddleocr import PaddleOCR # C0114, pylint: disable=missing-module-docstring
from typing import List
import numpy as np
import cv2


class Filter:
    """
    Filter for selecting words that the user wants to find from the words found by OCR processing.

    ...
    Attributes
    ----------
    _filter_words : list
        Words to filter.

    Methods
    -------
        set_filter(new_filter)
            Save words to filtering, setter to _filter_words (variable)
        get_filter()
            Returns the filter words    
    """

    def __init__(self, filter_:List[str]):
        """ TO DO """
        self._filter_words = filter_

    def set_filter(self, new_filter):
        """ TO DO """
        self._filter_words = new_filter

    def get_filter(self):
        """ TO DO """
        return self._filter_words

class Results:
    """
    Filter for selecting words that the user wants to find from the words found by OCR processing.

    ...
    Attributes
    ----------
    _filter_words : list
        Words to filter.

    Methods
    -------
        set_filter(new_filter)
            Save words to filtering, setter to _filter_words (variable)
        get_filter()
            Returns the filter words    
    """

    def __init__(self):
        """ TO DO """
        self._results = []

    def set_results(self, new_results):
        """ TO DO """
        self._results = new_results

    def get_results(self):
        """ TO DO """
        return self._results

def list_of_strings(arg):
    """ TO DO """
    return arg.split(',')

def read_imagefile(data):
    """ TO DO """
    npimg = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR) # E1101, pylint: disable=no-member
    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # E1101, pylint: disable=no-member
    return frame

def ocr_process(img, phrases):
    """ TO DO """
    ocr = PaddleOCR(use_angle_cls=True, lang="pt", show_log=False)  # Initialize PaddleOCR
    result = ocr.ocr(img, cls=True)  # Get OCR results for the input image

    # Extract relevant information from OCR results based on specified phrases
    structure_result = {
        "coord": [],
        "text_lines": [],
        "text_lines_sec": [],
        "boxes": [],
        "boxes_sec": [],
        "txts": [], 
        "num_boxes": None,
        "all_txts": None,
        "num_boxes_sec": None
    }


    for f in phrases:
        phrase = f.upper().replace(" ", "").replace("$","S")

        for idx in result:
            for line in idx:
                _line_plus = line[1][0].upper().replace(" ", "").replace("$","S")
                line_plus = _line_plus[: len(phrase)]

                if line_plus == phrase:
                    structure_result['coord'].append({line[1][0]: line[0]})
                    structure_result["text_lines"].append(line[1][0])
                    structure_result["boxes"].append(line[0])

                    if len(phrase) != len(_line_plus):
                        txts_ = line[1][0]
                        txts_ = txts_.split(f)
                        structure_result["txts"].append(txts_)

        # Process the found coordinates
        for comp in structure_result['coord']:
            product = next(iter(comp.keys()))
            coordinates = comp[product]

            xy_min = coordinates[0]
            xy_max = coordinates[2]

            print(f"\n\nCOORDENADA DO CAMPO ({product}) {xy_min, xy_max}\n")
            for l in result:
                for axis in l:
                    _xy_min = axis[0][0]
                    _xy_max = axis[0][2]

                    comparing_min = xy_min[1] / _xy_min[1]
                    comparing_max = xy_max[1] / _xy_max[1]

                    different = False
                    if (
                        xy_min[0] != _xy_min[0]
                        and xy_max[0] != _xy_max[0]
                        and xy_min[0] < _xy_min[0]
                        and xy_max[0] < _xy_max[0]
                    ):
                        different = True

                    if (
                        (comparing_min >= 0.98 and comparing_min <= 1.02)
                        and (comparing_max >= 0.98 and comparing_max <= 1.02)
                        and (different == True)
                        and (axis[0] not in structure_result["boxes"])
                    ):
                        print(
                            f"ACHOU, CAMPO ({axis[1][0]}), Coordenada {_xy_min, _xy_max}"
                        )
                        structure_result["text_lines_sec"].append(axis[1][0])
                        structure_result["boxes_sec"].append(axis[0])

        structure_result["num_boxes"] = len(structure_result["boxes"])
        structure_result["boxes"] = np.array(structure_result["boxes"]).reshape(structure_result["num_boxes"], 4, 2).astype(np.int64)

        structure_result["num_boxes_sec"] = len(structure_result["boxes_sec"])
        structure_result['boxes_sec'] = np.array(structure_result["boxes_sec"]).reshape(structure_result["num_boxes_sec"], 4, 2).astype(np.int64)

        structure_result['all_txts'] = np.concatenate((structure_result["text_lines"],
                                    structure_result["text_lines_sec"]), axis=0)

        return structure_result['all_txts'].tolist()
