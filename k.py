from PIL import ImageGrab,Image
# snapshot = ImageGrab.grab()
save_path = "C:\\Users\\Shiva Gagula\\Desktop\\Playment AI\\Media\\1.png"
# snapshot.save(save_path)

image = Image.open(save_path)
box = (10,410,675,730)
print(image.size)
cropped_image = image.crop(box)
save_path2 = "C:\\Users\\Shiva Gagula\\Desktop\\Playment AI\\Media\\2.png"
cropped_image.save(save_path2)

img = Image.open(save_path2)
img.show()
