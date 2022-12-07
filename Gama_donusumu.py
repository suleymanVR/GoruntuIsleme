import cv2
import numpy as np


def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread("C:/Users/Casper/Desktop/elma.jpg")
gammaImg = gammaCorrection(img, 4.4)

gammaImg = cv2.putText(gammaImg, 'Gama Donusumu = 4.4 ', (30,30) , cv2.FONT_HERSHEY_SIMPLEX,
                   0.6, (255, 0, 0) , 2, cv2.LINE_AA)

cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
