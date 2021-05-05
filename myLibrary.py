import cv2
import re
class ChessBoard:
    def __init__(self, img):
        self.img = img
        height = self.img.shape[0]
        self.height = (height/8)

    def resize(self,size):
        try:
            size = int(size)
            self.img = cv2.resize(self.img, (size,size), interpolation = cv2.INTER_AREA)
            self.height = size
        except:
            print('Enter a valid Size!')
            

    def drawing(self, block_name):
        regex = '[a-h][1-8]$'
        flag = 0
        while(not flag):
            if(re.match(regex,block_name)):
                col = ord(block_name[0]) - 96
                row = int(block_name[1])
                flag = 1
            else:
                print('Enter a valid Square!')
                block_name = input('Square: ')
        
        if((row+col)%2==0):
            cv2.circle(self.img, (round(self.height*(col-1)+(self.height/2)), round(self.height*(8-row)+(self.height/2))), round(self.height/2), (255, 255, 255), -1)
        else:
            cv2.circle(self.img, (round(self.height*(col-1)+(self.height/2)), round(self.height*(8-row)+(self.height/2))), round(self.height/2), (0, 0, 0), -1)

    def display(self):
        cv2.imshow('Frame', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()