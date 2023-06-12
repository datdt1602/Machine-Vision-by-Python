import cv2 #Xu li anh
from PIL import Image #Thu vien xu li anh ho tro nhieu loai anh
import numpy as np
import matplotlib.pyplot as plt #Ve bieu do histogram
import math


#Tao duong dan
filehinh = r'lena_1.jpg'
#Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL
imgPIL = Image.open(filehinh)

#Lay kich thuoc cua anh
height, width, channel = img.shape

#Khai bao cac bien de chua gia tri cac kenh mau
hue = Image.new(imgPIL.mode, imgPIL.size)
saturation = Image.new(imgPIL.mode, imgPIL.size)
intensity = Image.new(imgPIL.mode, imgPIL.size)
HSI = Image.new(imgPIL.mode, imgPIL.size)

#Dung vong for de doc het cac diem anh
for x in range(width):
    for y in range(height):

        #Lay gia tri R,G,B cua tung pixel va gan vao cac bien R,G,B
        T = imgPIL.getpixel((x,y))   
        R = T[0]
        G =T[1]
        B = T[2]    

        #Tinh theta
        t1 = ((R - G) + (R - B)) / 2
        t2 = math.sqrt((R - G) * (R - G) + (R - B)*(G - B))
        theta = math.acos(t1 / t2)
       

        #Tinh gia tri H
        H = 0
        if (B<= G):
            H = theta
        else :
            H = math.pi*2 - theta
        H = np.uint8(H*180/math.pi)
        

        #Tinh gia tri S
        Min = min(R,G,B)
        S = np.uint8((1 - 3*Min/(R+G+B))*255)

        #Tinh gia tri I
        I = np.uint8((R + G + B)/3)
        
        #Gán giá trị vừa tính cho từng kênh
        hue.putpixel((x,y),(H,H,H))
        saturation.putpixel((x,y),(S,S,S))
        intensity.putpixel((x,y),(I,I,I)) 
        HSI.putpixel((x,y),(I,S,H)) 

#Chuyển ảnh từ PIL sang OpenCv để hiển thị trên openCV
imgHue = np.array(hue)
imgIntensity = np.array(intensity)
imgSaturation = np.array(saturation)
imgHSI = np.array(HSI)

#Hiển thị hình dùng thư viện OpenCV
cv2.imshow('Anh goc RGB', img)
cv2.imshow('Kenh mau Hue', imgHue)
cv2.imshow('Kenh mau Intensity', imgIntensity)
cv2.imshow('Kenh mau Saturation', imgSaturation)
cv2.imshow('Hinh HSI', imgHSI)

#Bấm phím bất kì để đóng cửa sổ hiển thị hình
cv2.waitKey(0)

#Giai phong bo nho
cv2.destroyAllWindows()