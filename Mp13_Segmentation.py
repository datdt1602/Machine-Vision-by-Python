import cv2 
from PIL import Image # thư vien xu li anh
import numpy as np

filehinh = r"E:\Thi_Giac_May\lenna_color.jpg"
imgPIL = Image.open(filehinh)
img=cv2.imread("lenna_color.jpg", cv2.IMREAD_COLOR)

Segmentation =Image.new(imgPIL.mode,imgPIL.size)
width = imgPIL.size[0]
height = imgPIL.size[1]
#khai báo giá trị xy và ngưỡng
X1 = int(input("Nhập x1: "))
X2 = int(input("Nhập x2: "))
Y1 = int(input("Nhập y1: "))
Y2 = int(input("Nhập y2: "))
nguong = int(input("Nhập ngưỡng: "))
G_avg = 0
R_avg = 0
B_avg = 0
#Tính vecto Tb màu:
for x in range(X1,X2):
    for y in range(Y1,Y2):
        R,G,B=imgPIL.getpixel((x,y))
        R_avg += R
        G_avg += G
        B_avg += B

Size= (X2-X1+1)*(Y2-Y1+1)
R_avg= R_avg /Size
G_avg= G_avg /Size
B_avg= B_avg /Size

#Tính giá trị Euclidean Distance(z,a)
for x in range (width):
    for y in range(height):
        zR,zG,zB =imgPIL.getpixel((x,y))
        D0 = np.sqrt((zR - R_avg)**2 + (zG - G_avg)**2 + (zB - B_avg)**2)
        if D0 <nguong:
            Segmentation.putpixel((x,y),(255,255,255))
        else:
            Segmentation.putpixel((x,y),(zB,zG,zR))
img_Seg= np.array(Segmentation)
cv2.imshow('Hinh Goc', img)
cv2.imshow('Hinh phan doan mau ', img_Seg)
cv2.waitKey(0)
cv2.destroyAllWindows()