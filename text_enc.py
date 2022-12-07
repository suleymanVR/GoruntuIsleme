from PIL import Image
from PIL import ImageEnhance

image = Image.open("C:/Users/Casper/Desktop/imgen.jpg")
image.show()
curr_sharp = ImageEnhance.Sharpness(image)
new_sharp = 8.3
img_sharped = curr_sharp.enhance(new_sharp)
img_sharped.show()
