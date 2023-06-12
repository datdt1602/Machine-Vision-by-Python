import cv2 #Xu li anh
from PIL import Image #Thu vien xu li anh ho tro nhieu loai anh
import numpy as np
import matplotlib.pyplot as plt #Ve bieu do histogram

#Tao duong dan
filehinh = r'Lena.jpg'
#Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL
imgPIL = Image.open(filehinh)

#Lay kich thuoc cua anh
height, width, channel = img.shape

#Khai bao cac bien de chua gia tri kenh mau 
Y = Image.new(imgPIL.mode, imgPIL.size)
Cr = Image.new(imgPIL.mode, imgPIL.size)
Cb = Image.new(imgPIL.mode, imgPIL.size)
YCrCb = Image.new(imgPIL.mode, imgPIL.size)

#Dung vong for de doc het cac diem anh
for x in range(width):
    for y in range(height):

        #Lay gia tri R,G,B cua tung pixel va gan vao cac bien R,G,B
        R = img[y, x, 2]
        G = img[y, x, 1]
        B = img[y, x, 0]

        #Tính kênh XYZ theo công thức
        valueY = np.uint8(16 + (65.738 / 256) * R + (129.057 / 256) * G + (25.064 / 256) * B)
        valueCr = np.uint8(128 - (37.945 / 256) * R - (74.494 / 256) * G + (112.439 / 256) * B)
        valueCb = np.uint8(128 + (112.439 / 256) * R - (94.154 / 256) * G - (18.285 / 256) * B)
        
        #Gán giá trị vừa tính cho từng kênh
        Y.putpixel((x,y),(valueY,valueY,valueY))
        Cr.putpixel((x,y),(valueCr,valueCr,valueCr)) 
        Cb.putpixel((x,y),(valueCb,valueCb,valueCb))
        YCrCb.putpixel((x,y),(valueCb, valueCr, valueY)) 

#Chuyển ảnh từ PIL sang OpenCv để hiển thị trên openCV
imgY = np.array(Y)
imgCr = np.array(Cr)
imgCb = np.array(Cb)
imgYCrCb = np.array(YCrCb)


#Hiển thị hình dùng thư viện OpenCV
cv2.imshow('Anh goc RGB', img)
cv2.imshow('Kenh Y', imgY)
cv2.imshow('Kenh Cr', imgCr)
cv2.imshow('Kenh Cb', imgCb)
cv2.imshow('Hinh YCrCb', imgYCrCb)

#Bấm phím bất kì để đóng cửa sổ hiển thị hình
cv2.waitKey(0)

#Giai phong bo nho
cv2.destroyAllWindows()