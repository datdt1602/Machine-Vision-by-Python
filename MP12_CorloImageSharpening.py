import cv2 #Xu li anh
from PIL import Image #Thu vien xu li anh ho tro nhieu loai anh
import numpy as np

#Làm nét ảnh màu mặt nạ 3x3
def ColorImageSharpening3x3(imgPIL):
    #Tạo 1 ảnh cùng kích thước và mode với ảnh imgPIL
    #Ảnh này chứa kết quả cuyển đổi RGB to Grayscale
    SharpenImage = Image.new(imgPIL.mode, imgPIL.size)

    #Lấy kích thước của ảnh từ imgPIL
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
            SharpenR = 0
            SharpenG = 0
            SharpenB = 0
            #Tiến hành quét các điểm có trong mặt nạ
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    #Lấy thông tin màu R-G-B tại các điểm ảnh trong mặt nạ tại các vị trí (i,j)
                    R = img[y, x, 2]
                    G = img[y, x, 1]
                    B = img[y, x, 0]
                    #Nhâp tích chập các điểm ảnh đó cho mỗi kênh R-G-B tương ứng 
                    Rs += R*matran[i-x+1,j-y+1] 
                    Gs += G*matran[i-x+1,j-y+1]
                    Bs += B*matran[i-x+1,j-y+1]
            #Kết thúc quét và cộng dồn điểm ảnh trong mặt nạ 
            #Tính điểm sắc nét theo công thức 
            R1 = img[y, x, 2]
            G1 = img[y, x, 1]
            B1 = img[y, x, 0]
            SharpenR = R1 + Rs
            SharpenG = G1 + Gs
            SharpenB = B1 + Bs

            #Giới hạn các giá trị điểm ảnh
            if (SharpenR < 0):
                SharpenR = 0
            elif (SharpenR > 255):
                SharpenR = 255
            if (SharpenG < 0):
                SharpenG = 0
            elif (SharpenG > 255):
                SharpenG = 255
            if (SharpenB < 0):
                SharpenB = 0
            elif (SharpenB > 255):
                SharpenB = 255

            #Gán giá trị vừa tính cho từng kênh
            SharpenImage.putpixel((x,y),(SharpenB,SharpenG,SharpenR))
    return SharpenImage

#=========================================================
#CHƯƠNG TRÌNH CHÍNH

#Tao duong dan
filehinh = r'Lena.jpg'
#Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL
imgPIL = Image.open(filehinh)

#Mặt nạ ma trận làm nét
#array tạo mảng chứa ma trận mặt nạ
matran = np.array([[0, -1, 0 ],[-1, 4, -1],[ 0, -1, 0]])

#Chuyển ảnh sang mức xám
SharpenImage3 = ColorImageSharpening3x3(imgPIL)

#Chuyển ảnh PIL sang OpenCv để hiển thị bằng thư viện OpenCv
SharpenImageCV = np.array(SharpenImage3)

#hiển thị ảnh bằng thư viện OpenCv
cv2.imshow('Anh lam net ', SharpenImageCV)
cv2.imshow('Anh goc RGB', img)


# Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()