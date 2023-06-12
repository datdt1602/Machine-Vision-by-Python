import cv2          #Thư viện xử lí OpenCV cho python
import numpy as np       #Thư viện toán học, đặc biệt là tính toán ma trận

# Đọc ảnh màu dùng thư viện OpenCv
img = cv2.imread('Lena.jpg', cv2.IMREAD_COLOR)

#Lấy kích thước của ảnh
height, width, channel = img.shape

#height =len(img[0])
#width =len(img[1])

#Khai báo 3 biến để chứa 3 kênh màu RGB
red = np.zeros((height, width, 3), np.uint8) 
green = np.zeros((height, width, 3), np.uint8)
blue = np.zeros((height, width, 3), np.uint8)

#Set 0 cho tất cả điểm ảnh ban đầu có trong 3 kênh màu
red[:] =[0, 0, 0]
green[:] =[0, 0, 0]
blue[:] =[0, 0, 0]

#Đọc các pixel
for x in range(width):
    for y in range(height):
        R = img[y, x, 2]
        G = img[y, x, 1]
        B = img[y, x, 0]

        #Thiết lập màu cho các kênh 
        red[y, x, 2] = R
        green[y, x, 1] = G
        blue[y, x, 0] = B
# Hiển thị hình ảnh
cv2.imshow('Hinh mau RGB goc', img)
cv2.imshow('Kenh RED', red)
cv2.imshow('Kenh GREEN', green)
cv2.imshow('Kenh Blue', blue)
# Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phonhs bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()