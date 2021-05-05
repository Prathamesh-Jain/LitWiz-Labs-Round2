import numpy as np
import cv2
from myLibrary import *

img = cv2.imread('input_image.png')
Image = ChessBoard(img)
flag = 0
size_str = input('Size: ')
flag = 0
while(not flag):
    try:
        int(size)
        flag = 1
    except:
        print('Enter a valid Size!')
        size = input()
blockName = input('Square: ')
Image.drawing(blockName)
Image.resize(size)
Image.display()