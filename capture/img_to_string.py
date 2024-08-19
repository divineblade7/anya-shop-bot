import pytesseract

from config.get_config_values import get_tesseract_path


def imgToString(capture_attributes):
    pytesseract.pytesseract.tesseract_cmd = f"{get_tesseract_path()}\\tesseract.exe"
    attributes_img = capture_attributes()
    attributes = pytesseract.image_to_string(attributes_img)
    lines = attributes.splitlines()
    return lines, attributes_img
