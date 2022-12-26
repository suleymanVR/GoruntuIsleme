import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image and convert it to grayscale
image = cv2.imread("C:/Users/Casper/Desktop/elma.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the histogram
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(hist)
plt.show()
