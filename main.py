from myLibrary import *

img = cv2.imread('input_image.png')
Image = ChessBoard(img)
size_str = int(input('Size: '))
blockName = input('Square: ')
Image.drawing(blockName)
Image.resize(size_str)
Image.display()