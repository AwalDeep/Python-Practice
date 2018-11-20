# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:05:41 2018

@author: Awal
"""
from PIL import Image
import pytesseract


im=Image.open("H:/Projects/tesseract/img2.png")

text =pytesseract.image_to_string(im,lang='eng')

print(text)



