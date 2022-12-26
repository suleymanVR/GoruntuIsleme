import numpy as np
from scipy import ndimage

# Load the image
image = np.array(Image.open("C:/Users/Casper/Desktop/elma.jpg"))

# Create the Roberts cross kernel
kernel = np.array([[0, 0, 0],
                   [0, 1, 0],
                   [0, 0,-1]])

# Convolve the image with the kernel
filtered_image = ndimage.convolve(image, kernel)

# Display the filtered image
plt.imshow(filtered_image, cmap='gray')
plt.show()