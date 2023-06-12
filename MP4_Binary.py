import cv2          #Thư viện xử lí OpenCV cho python
from PIL import Image #Thư viện xữ lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh
import numpy as np       #Thư viện toán học, đặc biệt là tính toán ma trận

# Đọc ảnh màu dùng thư viện OpenCv
img = cv2.imread('Lena.jpg', cv2.IMREAD_COLOR)

#Đọc ảnh màu sử dụng thư viện PIL. Ảnh PIL dùng để xử lý và tính toán
imgPIL = Image.open('Lena.jpg')

#Tạo 1 ảnh cùng kích thước và mode với ảnh imgPIL
#Ảnh này chứa kết quả cuyển đổi RGB to Grayscale
binary = Image.new(imgPIL.mode, imgPIL.size)


#Lấy kích thước của ảnh từ imgPIL
width =binary.size[0]
height = binary.size[1]

#Thiết lập ngưỡng
nguong = 130
#Đọc các giá trị pixel
for x in range(width):
    for y in range(height):
        R = img[y, x, 2]
        G = img[y, x, 1]
        B = img[y, x, 0]

        #Dùng pp Luminance chuyển đổi RGB to Grayscale
        nhiphan = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)

        #Xác định giá rtrij điểm ảnh dựa vào ngưỡng
        if (nhiphan < nguong):
            binary.putpixel((x, y), (0, 0, 0))
        else:
            binary.putpixel((x, y), (255, 255, 255))
        

#Chuyển ảnh từ PIl sang OpenCv để hiển thị trên openCv
hinhnhiphan = np.array(binary)

# Hiển thị hình ảnh
cv2.imshow('Hinh mau RGB', img)
cv2.imshow('Hinh nhi phan Binary', hinhnhiphan)
# Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()