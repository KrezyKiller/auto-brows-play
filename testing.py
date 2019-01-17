import pytesseract
from PIL import ImageGrab,Image
import cv2
import os
import numpy as np

save_path2 = "C:/Users/Shiva Gagula/Desktop/Playment AI/Media/3.jpg"
save_path3 = "C:/Users/Shiva Gagula/Desktop/Playment AI/Media/4.jpg"

text = pytesseract.image_to_string(Image.open(save_path2))
print(text)



# img = cv2.imread(save_path2)
# cv2.imshow('image',img)
# re,img2 = cv2.threshold(img, 127, 125, cv2.THRESH_BINARY)
# cv2.imshow('image2',img2)
# cv2.imwrite('4.jpg',img2)
#
path = 'C:/Users/Shiva Gagula/Desktop/Playment AI/Media/'
# cv2.imwrite(os.path.join(path , '4.jpg'), img2)
#
#
# cv2.waitKey(0)
# text = pytesseract.image_to_string(Image.open(save_path3))
# print(text)



fname = save_path2
bgray = cv2.imread(fname)[...,0]

blured1 = cv2.medianBlur(bgray,3)
blured2 = cv2.medianBlur(bgray,51)
divided = np.ma.divide(blured1, blured2).data
normed = np.uint8(255*divided/divided.max())
th, threshed = cv2.threshold(normed, 100, 255, cv2.THRESH_OTSU)

dst = np.vstack((bgray, blured1, blured2, normed, threshed))
cv2.imwrite(os.path.join(path , '4.jpg'), dst)

text = pytesseract.image_to_string(Image.open(save_path2))
print(text)
