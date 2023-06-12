import cv2          #Thư viện xử lí OpenCV cho python
from PIL import Image #Thư viện xữ lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh
import numpy as np       #Thư viện toán học, đặc biệt là tính toán ma trận
import matplotlib.pyplot as plt #Thu vien vs bieu do

#======================================================
#Tinh histogram cua anh RGB
def TinhHistogram(HinhPIL):
    #Mỗi pĩel có giá trị từ 0-255
    #Khai báo mỗi mảng có 256 phần tử để chứa số đếm của các pĩels có cùng giá trị
    hisR = np.zeros(256)
    hisG = np.zeros(256)
    hisB = np.zeros(256)

    #Kích thước ảnh
    w = HinhPIL.size[0]
    h = HinhPIL.size[1]

    for x in range(w):
        for y in range(h):
            #Lấy giá trị mức xám tại điểm (x,y)
            gR, gG, gB = HinhPIL.getpixel((x,y))

            #Giá trị R tính ra cũng chính là phần tử thứ R trong mảng hisR đã khai báo ở trên
            #Tăng số đếm của phần tử thứ R lên 1. Tương tự với R, B
            hisR[gR] +=1
            hisG[gG] +=1
            hisB[gB] +=1

    return hisR, hisG, hisB #Trả về giá trị mảng Histogram

#Vẽ biểu đồ Histogram
def VeBieuDoHistogram(hisR, hisG, hisB):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram ảnh RFB', figsize=(((w, h))), dpi=100)
    trucX = np.zeros(256)
    trucX = np.linspace(0, 256, 256) 
    plt.plot(trucX, hisR, color='red')
    plt.plot(trucX, hisG, color='green')
    plt.plot(trucX, hisB, color='blue')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mau RGB')
    plt.ylabel('Số điểm cùng giá trị')
    plt.show()

    #=========================================================
#CHƯƠNG TRÌNH CHÍNH

# Khai báo đường dẫn file hình
filehinh = r'birdsmall.jpg'

#Đọc ảnh bằng OpenCv và hiển thị bằng thư viện OpenCv
HinhCV = cv2.imread(filehinh, cv2.IMREAD_COLOR)
cv2.imshow('Anh mau RGB', HinhCV)

#Đọc ảnh màu sử dụng thư viện PIL. Ảnh PIL dùng để xử lý và tính toán
HinhPIL = Image.open(filehinh)

#Tính Histogram
hisR, hisG, hisB = TinhHistogram(HinhPIL)

#Hiển thị biểu đồ Histogram
VeBieuDoHistogram(hisR, hisG, hisB)

# Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()