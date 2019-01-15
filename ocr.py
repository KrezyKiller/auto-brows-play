# import the necessary packages
from PIL import Image
import pytesseract


save_path2 = "C:/Users/Shiva Gagula/Desktop/Playment AI/2.png"


text = pytesseract.image_to_string(Image.open(save_path2))
print(text)
