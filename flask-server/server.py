# from flask import Flask
# app = Flask (__name__)
# @app.route("/members")
# def members():
#         return {"members":["mem1","mem2","mem3"]}
# if __name__=="__main__":
#         app.run(debug=True)
# from nis import match
from PIL import Image
import pytesseract
import spacy
import re

image_1='invoice.png'


img_obj_1=Image.open(image_1)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text_1 = pytesseract.image_to_string(img_obj_1)

nlp = spacy.load('en_core_web_sm')
doc = nlp(text_1)


date_entities = ['DATE']
org_entities = ['ORG', 'NORP']
address_entities = ['ADDRESS']
invoice_num_regex = r'([a-zA-Z]+[0-9]+)'

# Extract the relevant entities from the invoice
for entity in doc.ents:
    if entity.label_ in date_entities:
        print('Invoice Date:', entity.text)
    elif entity.label_ in org_entities:
        print('Vendor:', entity.text)
    elif entity.label_ in address_entities:
        print('Vendor Address:', entity.text)
    elif re.match(invoice_num_regex, entity.text):
        print('Invoice Number:', entity.text)

# print(text_1)