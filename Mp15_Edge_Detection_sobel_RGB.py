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
        Gradient = [[0, 0], [0, 0], [0, 0]]       
        for i in range(-1, 2):
            for j in range(-1, 2):
                R, G, B = imgPIL.getpixel((x + i, y + j))
                gray = 0.2126 * R + 0.7152 * G + 0.0722 * B
                Gradient[0] [0] += R * Sober_X[i + 1] [j + 1]
                Gradient[0] [1] += R * Sober_Y[i + 1] [j + 1]

                Gradient[1] [0] += G * Sober_X[i + 1] [j + 1]
                Gradient[1] [1] += G * Sober_Y[i + 1] [j + 1]

                Gradient[2] [0] += B * Sober_X[i + 1] [j + 1]
                Gradient[2] [1] += B * Sober_Y[i + 1] [j + 1]

                gxx = (Gradient[0][0] * Gradient[0][0]) + (Gradient[1][0] * Gradient[1][0]) + (Gradient[2][0] * Gradient[2][0])
                gyy = (Gradient[0][0] * Gradient[0][0]) + (Gradient[1][0] * Gradient[1][0]) + (Gradient[2][0] * Gradient[2][0])
                gxy = (Gradient[0][0] * Gradient[0][1]) + (Gradient[1][0] * Gradient[1][1]) + (Gradient[2][0] * Gradient[2][1])

                theta_xy = math.atan2((2 * gxy), (gxx - gyy)) / 2
                F0 = math.sqrt((gxx + gxy + (gxx - gyy) * math.cos(2 * theta_xy) + 2 * gxy * math.sin(2 * theta_xy)) / 2)

                if (F0 <= nguong):
                    ImageDetected.putpixel((x, y), (0, 0, 0))               
                else:
                    ImageDetected.putpixel((x, y), (255, 255, 255))

img_Detected = np.array(ImageDetected)
print("Nhan phim bat ki de tiep tuc..")
cv.imshow('Anh Goc', img)
cv.imshow('Anh Edge Detection_Sobel_RGB', img_Detected)
cv.waitKey(0)
cv.destroyAllWindows()