import cv2 #Xu li anh
from PIL import Image #Thu vien xu li anh ho tro nhieu loai anh
import numpy as np

#Làm mượt ảnh màu mặt nạ 3x3
def ColorImageSmoothing3x3(imgPIL):
    #Tạo 1 ảnh cùng kích thước và mode với ảnh imgPIL
    #Ảnh này chứa kết quả cuyển đổi RGB to Grayscale
    SmoothImage = Image.new(imgPIL.mode, imgPIL.size)

    #Lấy kích thước của ảnh từ imgPIL`
    width = imgPIL.size[0]
    height = imgPIL.size[1]
   
    #Đọc các giá trị pixel, dùng 2 vòng lặp for để đọc hết các pixel theo 2 chiều
    #Mặt nạ 3x3 có thể bỏ qua đường viền 1 pixel bên ngoài
    #X lấy tuwf 1 đến width -1, y lấy từ 1 tới height-1)
    for x  in range(1,width-1):
        for y in range(1,height-1):
            #Các biến này dùng để chứa các giá trị cộng dồn của các pixel trong mặt nạ
            Rs = 0
            Gs = 0
            Bs = 0
            #Tiến hành quét các điểm có trong mặt nạ
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    #Lấy thông tin màu R-G-B tại các điểm ảnh trong mặt nạ tại các vị trí (i,j)
                    R = img[y, x, 2]
                    G = img[y, x, 1]
                    B = img[y, x, 0]
                    #Cộng dồn các điểm ảnh đó cho mỗi kênh R-G-B tương ứng 
                    Rs += R
                    Gs += G
                    Bs += B
            K = 3 * 3 #mặt nạ 3x3
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)

            #Gán giá trị vừa tính cho từng kênh
            SmoothImage.putpixel((x,y),(Bs,Gs,Rs))
    return SmoothImage

#Làm mượt ảnh màu mặt nạ 5x5
def ColorImageSmoothing5x5(imgPIL):
    #Tạo 1 ảnh cùng kích thước và mode với ảnh imgPIL
    #Ảnh này chứa kết quả cuyển đổi RGB to Grayscale
    SmoothImage = Image.new(imgPIL.mode, imgPIL.size)

    #Lấy kích thước của ảnh từ imgPIL`
    width = imgPIL.size[0]
    height = imgPIL.size[1]
   
    #Đọc các giá trị pixel, dùng 2 vòng lặp for để đọc hết các pixel theo 2 chiều
    #Mặt nạ 5x5 có thể bỏ qua đường viền 2 pixel bên ngoài
    #X lấy tu 2 đến width -2, y lấy từ 2 tới height-2)
    for x  in range(2,width-2):
        for y in range(2,height-2):
            #Các biến này dùng để chứa các giá trị cộng dồn của các pixel trong mặt nạ
            Rs = 0
            Gs = 0
            Bs = 0
            #Tiến hành quét các điểm có trong mặt nạ
            for i in range(x-2,x+3):
                for j in range(y-2,y+3):
                    #Lấy thông tin màu R-G-B tại các điểm ảnh trong mặt nạ tại các vị trí (i,j)
                    R = img[y, x, 2]
                    G = img[y, x, 1]
                    B = img[y, x, 0]
                    #Cộng dồn các điểm ảnh đó cho mỗi kênh R-G-B tương ứng 
                    Rs += R
                    Gs += G
                    Bs += B
            K = 5 * 5 #mặt nạ 5x5
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)

            #Gán giá trị vừa tính cho từng kênh
            SmoothImage.putpixel((x,y),(Bs,Gs,Rs))
    return SmoothImage

#Làm mượt ảnh màu mặt nạ 7x7
def ColorImageSmoothing7x7(imgPIL):
    #Tạo 1 ảnh cùng kích thước và mode với ảnh imgPIL
    #Ảnh này chứa kết quả cuyển đổi RGB to Grayscale
    SmoothImage = Image.new(imgPIL.mode, imgPIL.size)

    #Lấy kích thước của ảnh từ imgPIL`
    width = imgPIL.size[0]
    height = imgPIL.size[1]
   
    #Đọc các giá trị pixel, dùng 2 vòng lặp for để đọc hết các pixel theo 2 chiều
    #Mặt nạ 7x7 có thể bỏ qua đường viền 3 pixel bên ngoài
    #X lấy tu 3 đến width - 3, y lấy từ 3 tới height-3)
    for x  in range(3,width-3):
        for y in range(3,height-3):
            #Các biến này dùng để chứa các giá trị cộng dồn của các pixel trong mặt nạ
            Rs = 0
            Gs = 0
            Bs = 0
            #Tiến hành quét các điểm có trong mặt nạ
            for i in range(x-3,x+4):
                for j in range(y-3,y+4):
                    #Lấy thông tin màu R-G-B tại các điểm ảnh trong mặt nạ tại các vị trí (i,j)
                    R = img[y, x, 2]
                    G = img[y, x, 1]
                    B = img[y, x, 0]
                    #Cộng dồn các điểm ảnh đó cho mỗi kênh R-G-B tương ứng 
                    Rs += R
                    Gs += G
                    Bs += B
            K = 7 * 7 #mặt nạ 7x7
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)

            #Gán giá trị vừa tính cho từng kênh
            SmoothImage.putpixel((x,y),(Bs,Gs,Rs))
    return SmoothImage

#Làm mượt ảnh màu mặt nạ 9x9
def ColorImageSmoothing9x9(imgPIL):
    #Tạo 1 ảnh cùng kích thước và mode với ảnh imgPIL
    #Ảnh này chứa kết quả cuyển đổi RGB to Grayscale
    SmoothImage = Image.new(imgPIL.mode, imgPIL.size)

    #Lấy kích thước của ảnh từ imgPIL`
    width = imgPIL.size[0]
    height = imgPIL.size[1]
   
    #Đọc các giá trị pixel, dùng 2 vòng lặp for để đọc hết các pixel theo 2 chiều
    #Mặt nạ 9x9 có thể bỏ qua đường viền 4 pixel bên ngoài
    #X lấy tu 4 đến width -4, y lấy từ 4 tới height-4)
    for x  in range(4,width-4):
        for y in range(4,height-4):
            #Các biến này dùng để chứa các giá trị cộng dồn của các pixel trong mặt nạ
            Rs = 0
            Gs = 0
            Bs = 0
            #Tiến hành quét các điểm có trong mặt nạ
            for i in range(x-4,x+5):
                for j in range(y-4,y+5):
                    #Lấy thông tin màu R-G-B tại các điểm ảnh trong mặt nạ tại các vị trí (i,j)
                    R = img[y, x, 2]
                    G = img[y, x, 1]
                    B = img[y, x, 0]
                    #Cộng dồn các điểm ảnh đó cho mỗi kênh R-G-B tương ứng 
                    Rs += R
                    Gs += G
                    Bs += B
            K = 9 * 9 #mặt nạ 9x9
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)

            #Gán giá trị vừa tính cho từng kênh
            SmoothImage.putpixel((x,y),(Bs,Gs,Rs))
    return SmoothImage
#=========================================================
#CHƯƠNG TRÌNH CHÍNH

#Tao duong dan
filehinh = r'Lena.jpg'
#Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL
imgPIL = Image.open(filehinh)

#Chuyển ảnh sang mức xám
SmoothImage3 = ColorImageSmoothing3x3(imgPIL)
SmoothImage5 = ColorImageSmoothing5x5(imgPIL)
SmoothImage7 = ColorImageSmoothing7x7(imgPIL)
SmoothImage9 = ColorImageSmoothing9x9(imgPIL)

#Chuyển ảnh PIL sang OpenCv để hiển thị bằng thư viện OpenCv
SmoothImageCV3 = np.array(SmoothImage3)
SmoothImageCV5 = np.array(SmoothImage5)
SmoothImageCV7 = np.array(SmoothImage7)
SmoothImageCV9 = np.array(SmoothImage9)
#hiển thị ảnh bằng thư viện OpenCv
cv2.imshow('Anh lam muot (3x3) ', SmoothImageCV3)
cv2.imshow('Anh lam muot (5x5) ', SmoothImageCV5)
cv2.imshow('Anh lam muot (7x7) ', SmoothImageCV7)
cv2.imshow('Anh lam muot (9x9) ', SmoothImageCV9)
cv2.imshow('Anh goc RGB', img)


# Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()