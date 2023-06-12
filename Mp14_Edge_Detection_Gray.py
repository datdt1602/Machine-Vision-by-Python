import cv2 as cv
import numpy as np    
from PIL import Image
import math
img = cv.imread("lenna_color.jpg", cv.IMREAD_COLOR)
imgPIL = Image.open('lenna_color.jpg')

nguong = int(input("Nhập ngưỡng: "))
print("Waiting...")

class imageSize:
    height, width, _ = img.shape

ImageDetected = Image.new(imgPIL.mode, imgPIL.size)

Sober_X = [ [ -1, -2, -1 ], [ 0, 0, 0 ], [ 1, 2, 1 ] ]
Sober_Y = [ [ -1, 0, 1 ], [ -2, 0, 2 ], [ -1, 0, 1 ] ]

for x in range(1, imageSize.width - 1):
    for y in range(1, imageSize.height - 1):    
        Gradient = [0,0]

        for i in range(-1, 2):
            for j in range(-1, 2):
                R = imgPIL.getpixel((x + i, y + j))
                G = imgPIL.getpixel((x + i, y + j))
                B = imgPIL.getpixel((x + i, y + j))
                
                # Chuyển đổi R, G, B sang kiểu số thực
                R = float(R[0])
                G = float(G[1])
                B = float(B[2])

                gray = 0.2126 * R + 0.7152 * G + 0.0722 * B
                Gradient[0] += gray * Sober_X[i + 1][ j + 1]
                Gradient[1] += gray * Sober_Y[i + 1][ j + 1]
                M = abs(Gradient[0]) + abs(Gradient[1])
                if (M <= nguong):
                    ImageDetected.putpixel((x, y), (0, 0, 0))
                
                else:
                    ImageDetected.putpixel((x, y), (255, 255, 255))

img_Detected = np.array(ImageDetected)

cv.imshow('Anh Goc', img)
cv.imshow('Anh Edege Detection Gray', img_Detected)
cv.waitKey(0)
cv.destroyAllWindows()
 