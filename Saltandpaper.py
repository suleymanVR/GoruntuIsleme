import random
import numpy as np
import cv2

# Read in the image
image = cv2.imread("C:/Users/Casper/Desktop/elma.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a blank image with the same dimensions as the original
filtered_image = np.zeros((gray_image.shape[0], gray_image.shape[1]), dtype=np.uint8)

# Iterate through each pixel in the image
for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        # Use a random number to determine if the pixel should be turned to black or white
        if random.random() < 0.1:
            if random.random() < 0.5:
                filtered_image[i, j] = 0  # black
            else:
                filtered_image[i, j] = 255  # white
        else:
            filtered_image[i, j] = gray_image[i, j]

# Save the filtered image
cv2.imwrite('saltandpaper_image.jpg', filtered_image)