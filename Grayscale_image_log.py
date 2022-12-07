import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Casper/Desktop/apple.jpeg")

image.shape
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap= 'gray')

# Apply log transformation method
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype = np.uint)

plt.imshow(image)
plt.show()
plt.imshow(log_image)
plt.show()
