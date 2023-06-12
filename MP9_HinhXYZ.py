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
X = Image.new(imgPIL.mode, imgPIL.size)
Y = Image.new(imgPIL.mode, imgPIL.size)
Z = Image.new(imgPIL.mode, imgPIL.size)
XYZ = Image.new(imgPIL.mode, imgPIL.size)

#Dung vong for de doc het cac diem anh
for x in range(width):
    for y in range(height):

        #Lay gia tri R,G,B cua tung pixel va gan vao cac bien R,G,B
        R = img[y, x, 2]
        G = img[y, x, 1]
        B = img[y, x, 0]   

        #Tính kênh XYZ theo công thức
        valueX = np.uint8(0.4124564 * R + 0.3575761 * G + 0.1804375 * B)
        valueY = np.uint8(0.2126729 * R + 0.7151522 * G + 0.0721750 * B)
        valueZ = np.uint8(0.0193339 * R + 0.1191920 * G + 0.9503041 * B)
        
        #Gán giá trị vừa tính cho từng kênh
        X.putpixel((x,y),(valueX,valueX,valueX))
        Y.putpixel((x,y),(valueY,valueY,valueY))
        Z.putpixel((x,y),(valueZ,valueZ,valueZ)) 
        XYZ.putpixel((x,y),(valueZ, valueY, valueX)) 

#Chuyển ảnh từ PIL sang OpenCv để hiển thị trên openCV
imgX = np.array(X)
imgZ = np.array(Z)
imgY = np.array(Y)
imgXYZ = np.array(XYZ)


#Hiển thị hình dùng thư viện OpenCV
cv2.imshow('Anh goc RGB', img)
cv2.imshow('Kenh mau X', imgX)
cv2.imshow('Kenh mau Z', imgZ)
cv2.imshow('Kenh mau Y', imgY)
cv2.imshow('Hinh XYZ', imgXYZ)

#Bấm phím bất kì để đóng cửa sổ hiển thị hình
cv2.waitKey(0)

#Giai phong bo nho
cv2.destroyAllWindows()