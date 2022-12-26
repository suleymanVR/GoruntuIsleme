import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/Casper/Desktop/elma.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Prewitt filter
prewitt_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
prewitt_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
prewitt = np.sqrt(np.square(prewitt_x) + np.square(prewitt_y))
prewitt = np.uint8(prewitt)

# Save the filtered image
cv2.imwrite('prewitt_image.jpg', prewitt)