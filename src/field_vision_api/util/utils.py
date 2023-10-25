""" 
Developed by: BRAIN - Brazilian Artificial Inteligence Nucleus
--------------------------------------------------------------
Developers: Natanael Vitorino, Lucas Oliveira and Pedro Santos
---
e-mail: natanael.vitorino@facens.br, lucas.camargo@facens.br 
        and pedro.santos@facens.br
---        
BRAIN, Sorocaba, Brazil, 2023
--------------------------------------------------------------
Description: A system for processing text on invoices, with 
the aim of identifying relevant fields on an invoice and 
optimizing rebate or validation systems. Making life easier 
for logistics operators, merchants and managers, the 
application has an interface that captures webcam images, 
processes the image using OCR and makes it possible to view 
the results obtained.
...
OCR PROCESSING
"""
from paddleocr import PaddleOCR # C0114, pylint: disable=wrong-import-order
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

    def __init__(self, filter_:List[str]) -> None:
        """ 
        Constructor for filter words class.

        ...
        Args:
            Without args.

        Returns:
            Without returns..
        """
        self._filter_words = filter_

    def set_filter(self, new_filter) -> None:
        """ 
        Setter for filter words.

        ...
        Args:
            Without args.

        Returns:
            Without returns.
        """
        self._filter_words = new_filter

    def get_filter(self) -> list:
        """ 
        Getter for filter words.

        ...
        Args:
            Without args.

        Returns:
            The filter words.
        """
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

    def __init__(self) -> None:
        """ 
        Constructor to Results class

        ...
        Args:
            None

        Returns:
            None
        """
        self._results = []

    def set_results(self, new_results) -> None:
        """ 
        Setter for OCR processing results.

        ...
        Args:
            new_results : Results from OCR processing.

        Returns:
            without return.
        """
        self._results = new_results

    def get_results(self) -> list:
        """ 
        Getter for OCR processing results.

        ...
        Args:
            Without args.

        Returns:
            The results.
        """
        return self._results


def list_of_strings(arg) -> list:
    """ 
    Get list of strings from user's filter input.

    ...
    Args:
        arg: Words taken from user input.

    Returns:
        The words entered by the user.
    """
    return arg.split(',')


def read_imagefile(data) -> np.ndarray:
    """ 
    Image processing.

    ...
    Args:
        data: API buffer image.

    Returns:
        Frame with rgb color pattern and processed from byte array to ndarray.
    """
    npimg = np.frombuffer(data, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR) # E1101, pylint: disable=no-member
    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # E1101, pylint: disable=no-member
    return frame

def ocr_process(img) -> list:
    """ 
    OCR processing.

    ...
    Args:
        img: image to process.

    Returns:
        Result of OCR processing on the image.
    """
    ocr = PaddleOCR(use_angle_cls=True, lang="pt", show_log=False)  # Initialize PaddleOCR
    result = ocr.ocr(img, cls=True)  # Get OCR results for the input image
    return result


def filter_process(result, phrases) -> list:
    """ 
    Filter processing.

    ...
    Args:
        img: image to process.
        phrases: words filter.

    Returns:
        The word of interest based on the filter reference.
    """

    # Extract relevant information from OCR results based on specified phrases
    management_data = {
        'line_plus': [],
        'txts_': None,
        'product': [],
        'coordinates': [],
        'xy_min': [],
        'xy_max': [],
        '_xy_min': [],
        '_xy_max': [],
        'comparing_min': [],
        'comparing_max': [],
    }

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

    # Find the target word and get the result using the filters
    for f in phrases: # R1702, pylint: disable=too-many-nested-blocks
        phrase = f.upper().replace(" ", "").replace("$","S")

        for idx in result:
            for line in idx:
                management_data['line_plus'] = line[1][0].upper().replace(" ", "").replace("$","S")
                management_data['line_plus'] = management_data['line_plus'][:len(phrase)]

                if management_data['line_plus'] == phrase:
                    structure_result['coord'].append({line[1][0]: line[0]})
                    structure_result["text_lines"].append(line[1][0])
                    structure_result["boxes"].append(line[0])

                    if len(phrase) != len(management_data['line_plus']):
                        management_data["txts_"] = line[1][0]
                        management_data["txts_"] = management_data["txts_"].split(f)
                        structure_result["txts"].append(management_data["txts_"])

        # Process the found coordinates
        for comp in structure_result['coord']:
            management_data["product"] = next(iter(comp.keys()))
            management_data["coordinates"] = comp[management_data["product"]]

            management_data["xy_min"] = management_data["coordinates"][0]
            management_data["xy_max"] = management_data["coordinates"][2]

            print(f"\n\nCOORDENADA DO CAMPO \
                ({management_data['product']}) \
                {management_data['xy_min'], management_data['xy_max']}\n")

            for l in result:
                for axis in l:
                    management_data['_xy_min'] = axis[0][0]
                    management_data['_xy_max'] = axis[0][2]

                    comparing_min = management_data['xy_min'][1] / management_data['_xy_min'][1]
                    comparing_max = management_data['xy_max'][1] / management_data['_xy_max'][1]

                    management_data['different'] = False

                    # Find the data on the same axis to the right of the reference
                    if (
                        management_data['xy_min'][0] < management_data['_xy_min'][0] and
                        management_data['xy_max'][0] < management_data['_xy_max'][0]
                    ):

                        # Checks the distance of the data from the reference
                        if (0.98 <= comparing_min <= 1.02 and
                           0.98 <= comparing_max <= 1.02 and
                           axis[0] not in structure_result["boxes"]):
                            print(
                                f"ACHOU, CAMPO ({axis[1][0]}), Coordenada \
                                {management_data['_xy_min'], management_data['_xy_max']}"
                            )
                            structure_result["text_lines_sec"].append(axis[1][0])
                            structure_result["boxes_sec"].append(axis[0])

        structure_result["num_boxes"] = len(structure_result["boxes"])
        structure_result["boxes"] = np.array(structure_result["boxes"]).reshape( # E1121, pylint: disable=too-many-function-args
                                    structure_result["num_boxes"], 4, 2).astype(np.int64)

        structure_result["num_boxes_sec"] = len(structure_result["boxes_sec"])
        structure_result['boxes_sec'] = np.array(structure_result["boxes_sec"])
        structure_result['boxes_sec'] = structure_result['boxes_sec'].reshape( #E1101, pylint: disable=no-member
                                        structure_result["num_boxes_sec"], 4, 2).astype(np.int64)

        structure_result['all_txts'] = np.concatenate((structure_result["text_lines"],
                                    structure_result["text_lines_sec"]), axis=0)

        return structure_result['all_txts'].tolist()
