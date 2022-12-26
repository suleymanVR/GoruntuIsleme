from PIL import Image

def rgb_to_hsl(rgb):
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    diff = cmax - cmin
    h = 0
    s = 0
    l = (cmax + cmin) / 2
    if diff != 0:
        if cmax == r:
            h = (g - b) / diff
        elif cmax == g:
            h = (b - r) / diff + 2
        elif cmax == b:
            h = (r - g) / diff + 4
        h *= 60
        if h < 0:
            h += 360
        s = diff / (1 - abs(2 * l - 1))
    return h, s, l

def convert_image_to_hsl(image):
    image = image.convert("RGB")
    hsl_image = Image.new("RGB", image.size)
    pixels = image.load()
    hsl_pixels = hsl_image.load()
    for x in range(image.width):
        for y in range(image.height):
            h, s, l = rgb_to_hsl(pixels[x, y])
            hsl_pixels[x, y] = (int(h), int(s * 255), int(l * 255))
    return hsl_image

# Example usage:
image = Image.open("C:/Users/Casper/Desktop/elma.jpg")
hsl_image = convert_image_to_hsl(image)
hsl_image.save("image_hsl.jpg")
