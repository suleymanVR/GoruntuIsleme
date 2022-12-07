from PIL import Image
Img1 = Image.open ("C:/Users/Casper/Desktop/apple.jpeg")
h,w = Img1.size
img = Img1.load()
for i in range(0,h):
    for j in range(0,w):
        R,G,B = img[i,j]
        R = 255 - R
        G = 255 - G
        B = 255 - B
        img[i,j] = (R,G,B)
Img1.show()