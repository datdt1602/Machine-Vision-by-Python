import cv2 
from PIL import Image
import numpy as np
import math

# Khai báo đường dẫn file hình
filehinh = r'lena_1.jpg'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

# Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này dùng để thực hiện các tác vụ xử lý & tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)

# Tạo 1 ảnh có cùng Mode và kích thước với ảnh imgPIL, dùng để chứa kết quả chuyển đổi RGB sang grayScale
Hue = Image.new(imgPIL.mode, imgPIL.size)
Saturation = Image.new(imgPIL.mode, imgPIL.size)
Value = Image.new(imgPIL.mode, imgPIL.size)
HSVimg = Image.new(imgPIL.mode, imgPIL.size)

# Lấy kích thước ảnh
width = imgPIL.size[0]
height = imgPIL.size[1]

# Mỗi ảnh là một ma trận 2 chiều nên sẽ dùng 2 vòng for để
# đọc hết các điểm ảnh (pixel) có trong hình
for x in range(width):
    for y in range(height):

        #Lấy giá trị điểm ảnh tại vị trí (x,y)
        R,G,B = imgPIL.getpixel((x,y))
        MIN = min(R,G,B)
        SUM = (R+G+B)
        MAX = max(R,G,B)

        # Theo công thức trong sách, t1 là phần tử của công thức
        t1 = ((R-G) + (R-B))/2

        # t2 là phần tử mẫu của công thức tính theta
        t2 = math.sqrt((R-G)*(R-G) + (R-B)*(G-B))

        # Chú ý: kết quả trả về của hàm tính acos trong công thức là radian
        theta = math.acos(t1/t2)

        # Công thức giá trị Hue
        h = 0

        # Nếu mà Blue <= Green thì Hue = Theta
        if B <= G:
            h = theta
        else:
            # Do theta là radian tính ở trên nên thay vì dùng 360 thì dùng pi
            h = 2*math.pi - theta

        # Chuyển đổi giá trị radian sang degree
        h = np.uint8(h*180/math.pi)

        # Công thức tính giá trị Saturation
        s = 1 - 3*MIN/SUM
            
        # Do giá trị tính ra của S nằm trong khoảng [0,1], để hiện thị được mình cần phải convert S sang khoảng
        # giá trị [0,255], công thức dưới đây chuyển đổi từ [0,1] sang [0,255]
        s = np.uint8(s*255)

        # Công thức tính giá trị kênh Intensity
        v = np.uint8(MAX)
            
        Hue.putpixel((x,y),(h,h,h))
        Saturation.putpixel((x,y),(s,s,s))
        Value.putpixel((x,y),(v,v,v))
        HSVimg.putpixel((x,y),(v,s,h))

imgH = np.array(Hue)
imgS = np.array(Saturation)
imgI = np.array(Value)
imgHSV = np.array(HSVimg)

# Hiện thị ảnh dung thư viện OpenCV
cv2.imshow('Anh RGB goc',img)
cv2.imshow('Kenh Hue',imgH)
cv2.imshow('Kenh Saturation',imgS)
cv2.imshow('Kenh Value',imgI)
cv2.imshow('Kenh HSV',imgHSV)

# Bấm phím bất kì để đóng cửa sổ hiện thị hình
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiện thị hình
cv2.destroyAllWindows()