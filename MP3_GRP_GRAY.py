import cv2          #Thư viện xử lí OpenCV cho python
from PIL import Image #Thư viện xữ lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh
import numpy as np       #Thư viện toán học, đặc biệt là tính toán ma trận

# Đọc ảnh màu dùng thư viện OpenCv
img = cv2.imread('Lena.jpg', cv2.IMREAD_COLOR)

#Đọc ảnh màu sử dụng thư viện PIL. Ảnh PIL dùng để xử lý và tính toán
imgPIL = Image.open('Lena.jpg')

#Tạo 1 ảnh cùng kích thước và mode với ảnh imgPIL
#Ảnh này chứa kết quả cuyển đổi RGB to Grayscale
average = Image.new(imgPIL.mode, imgPIL.size)
light = Image.new(imgPIL.mode, imgPIL.size)
lum = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước của ảnh từ imgPIL
width =average.size[0]
height = average.size[1]
width =light.size[0]
height = light.size[1]
width =lum.size[0]
height = lum.size[1]

#Đọc các giá trị pixel
for x in range(width):
    for y in range(height):
        R = img[y, x, 2]
        G = img[y, x, 1]
        B = img[y, x, 0]
        #Dùng pp Average chuyển đổi RGB to Grayscale
        gray = np.uint8((R + G + B) / 3)

        #Dùng pp Lightness chuyển đổi RGB to Grayscale
        MIN = min(R, G, B)
        MAX =max(R, G, B)
        gray1 = np.uint8((MIN + MAX) / 2)

        #Dùng pp Luminance chuyển đổi RGB to Grayscale
        gray2 = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)

        #Gán giá trị mức xám vừa tính cho ảnh xám
        average.putpixel((x, y), (gray, gray, gray))
        light.putpixel((x, y), (gray1, gray1, gray1))
        lum.putpixel((x, y), (gray2, gray2, gray2))
        #Ảnh có 3 kênh màu nên cho cùng giá trị

#Chuyển ảnh từ PIl sang OpenCv để hiển thị trên openCv
anhmucxam = np.array(average)
anhmucxam1 = np.array(light)
anhmucxam2 = np.array(lum)
# Hiển thị hình ảnh
cv2.imshow('Hinh mau RGB', img)
cv2.imshow('Hinh muc xam Average', anhmucxam)
cv2.imshow('Hinh muc xam Lightness', anhmucxam1)
cv2.imshow('Hinh muc xam Luminance', anhmucxam2)
# Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()