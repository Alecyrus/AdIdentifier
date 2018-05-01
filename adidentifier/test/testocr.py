# -*- coding: UTF-8 -*-

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract


tessdata_dir_config = '--tessdata-dir "/usr/local/share/tessdata"'
# Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# It's important to add double quotes around the dir path.
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

print(pytesseract.image_to_string(Image.open('1.jpg'), lang='chi_sim', config=tessdata_dir_config))


# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
print("\n\n")
# Simple image to string
print(pytesseract.image_to_string(Image.open('2.png')))


# Get verbose data including boxes, confidences, line and page numbers
#print(pytesseract.image_to_data(Image.open('test.png')))

#