import pytesseract
from PIL import ImageGrab,Image
import cv2
import os
import numpy as np

save_path3 = "C:/Users/Shiva Gagula/Desktop/Playment AI/Media/3.jpg"
path = 'C:/Users/Shiva Gagula/Desktop/Playment AI/Media/'

def imgprocess():

    fname = save_path3
    bgray = cv2.imread(fname)[...,0]

    blured1 = cv2.medianBlur(bgray,3)
    blured2 = cv2.medianBlur(bgray,51)
    divided = np.ma.divide(blured1, blured2).data
    normed = np.uint8(255*divided/divided.max())
    th, threshed = cv2.threshold(normed, 100, 255, cv2.THRESH_OTSU)

    dst = np.vstack((bgray, blured1, blured2, normed, threshed))
    cv2.imwrite(os.path.join(path , '4.jpg'), dst)
