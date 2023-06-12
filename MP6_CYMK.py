import cv2          #Thư viện xử lí OpenCV cho python
from PIL import Image #Thư viện xữ lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh
import numpy as np       #Thư viện toán học, đặc biệt là tính toán ma trận

#Đọc ảnh màu dùng thư viện openCV
img = cv2.imread('Lena.jpg', cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL:
imgPIL = Image.open('Lena.jpg')

#Tạo một ảnh có cùng kích thướca và mode với ảnh imgPIL:
cyan = Image.new(imgPIL.mode, imgPIL.size)
magenta= Image.new(imgPIL.mode, imgPIL.size)
yellow = Image.new(imgPIL.mode, imgPIL.size)
black = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước ảnh:
width = imgPIL.size[0]
height = imgPIL.size[1]

#Đọc điểm ảnh:
for x in range(width):
    for y in range(height):
        #Lấy giá trị điểm ảnh tại x,y:-
        R = imgPIL.getpixel((x,y)) 
        G = imgPIL.getpixel((x,y))
        B = imgPIL.getpixel((x,y))

        Red= np.uint8(R[0])
        Green = np.uint8(G[1])
        Blue = np.uint8(B[2])

        #Màu Cyan kết hợp giữa kênh Green và Blue:
        cyan.putpixel((x,y), (Blue, Green, 0))

        #Màu magenta kết hợp giữa kênh R và b:
        magenta.putpixel((x,y),(Blue, 0, Red))

        #yellow kết hợp giữa kênh R và G:
        yellow.putpixel((x, y), (0 ,Green ,Red))

        #Black lag lấy giá trị nhỏ nhất của R, G, B:
        K = np.min([Blue, Green, Red])
        black.putpixel((x,y),(K, K ,K))
# Chuyển ảnh từ PIl sang OpenCV:
imgC = np.array(cyan)
imgM = np.array(magenta)
imgY = np.array(yellow)
imgB = np.array(black)


#Hiển thị hình dùng thư viện OpenCV
cv2.imshow('Anh goc', img)
cv2.imshow('Kenh mau Cyan', imgC)
cv2.imshow('Kenh mau Magenta', imgM)
cv2.imshow('Kenh mau Yellow', imgY)
cv2.imshow('Kenh mau Black', imgB)

#BẤm phím bất kì 
cv2.waitKey(0)

#Giải phóng bộ nhớ
cv2.destroyAllWindows()