from PIL import ImageGrab,Image
import pytesseract


#capturing screen
snapshot = ImageGrab.grab()
save_path = "C:\\Users\\Shiva Gagula\\Desktop\\Playment AI\\Media\\1.jpg"
snapshot.save(save_path)

#croping image
image = Image.open(save_path)
box = (10,410,675,730)
print(image.size)
cropped_image = image.crop(box)
save_path2 = "C:\\Users\\Shiva Gagula\\Desktop\\Playment AI\\Media\\2.jpg"
cropped_image.save(save_path2)

#OCR converter
save_path2 = "C:/Users/Shiva Gagula/Desktop/Playment AI/Media/2.jpg"
text = pytesseract.image_to_string(Image.open(save_path2))
print(text)
