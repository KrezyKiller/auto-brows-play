from PIL import ImageGrab,Image
import pytesseract
import cv2
from .cvimag import imgprocess

__save_path1 = "C:\\Users\\Shiva Gagula\\Desktop\\Playment AI\\Media\\1.jpg"
__save_path2 = "C:\\Users\\Shiva Gagula\\Desktop\\Playment AI\\Media\\2.jpg"
__save_path3 = "C:\\Users\\Shiva Gagula\\Desktop\\Playment AI\\Media\\3.jpg"
__save_path4 = "C:\\Users\\Shiva Gagula\\Desktop\\Playment AI\\Media\\4.jpg"


def __screenshot():
    snapshot = ImageGrab.grab()
    snapshot.save(__save_path1)

def __crop():
    # croping image
    image = Image.open(__save_path1)
    box = (10, 410, 675, 730)
    cropped_image = image.crop(box)
    cropped_image.save(__save_path2)

    image = Image.open(__save_path1)
    box2 = (750,180,1240,220)
    cropped_image2 = image.crop(box2)
    cropped_image2.save(__save_path3)

def __imgpreprocess():
    pass

def __ocr():
    # OCR converter
    text1 = pytesseract.image_to_string(Image.open(__save_path2))
    # imgprocess()
    text2 = pytesseract.image_to_string(Image.open(__save_path3))
    return [text1,text2]

def ans():
      __screenshot()
      __crop()
      return __ocr()
