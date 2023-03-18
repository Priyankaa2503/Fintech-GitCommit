# from flask import Flask
# app = Flask (__name__)
# @app.route("/members")
# def members():
#         return {"members":["mem1","mem2","mem3"]}
# if __name__=="__main__":
#         app.run(debug=True)
from PIL import Image
import pytesseract

image_1='image1.png'


img_obj_1=Image.open(image_1)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text_1 = pytesseract.image_to_string(img_obj_1)
print(text_1)