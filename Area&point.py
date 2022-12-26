from PIL import Image

# Load the image
image = Image.open("C:/Users/Casper/Desktop/elma.jpg")

# Select the area of the image to focus on
area = (100, 100, 200, 200)

# Pick a point within the selected area
point = (150, 150)

# Display the whole image
image.show()
