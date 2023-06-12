import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image,ImageOps
from tkinter import filedialog
import cv2 as cv
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np

np.set_printoptions(suppress=True)

# Load the model
model = load_model(r'model.h5', compile=False)

#Giao diện bìapip install tk

def run():
    global anhbia
    anhbia.destroy()
#Tạo cửa sổ giao diện
anhbia = tk.Tk() #Đặt cửa sổ giao diện tên anhbia
anhbia.geometry("720x720")
anhbia.title("VEHICLE CLASSIFICATION")
# Mô hình ảnh bìa
anh=Image.open("BIA0.png")
# Chỉnh kích thước ảnh
resizeimage=anh.resize((720, 720))
a = ImageTk.PhotoImage(resizeimage)
img=tk.Label(image=a)
img.grid(column=0,row=0)
#Nút nhấn START
Btn=tk.Button(anhbia,text="START",font=("Constantia",20,'bold'),bg= 'green',fg='black',command= run )
Btn.place(x=200,y=620)
anhbia.mainloop() #Lặp lại câu lệnh của anhbia để hiện cửa sổ liên tục = giữ cửa sổ hiển thị

#Set up cái đối tượng trong giao diện chính (trang tiếp theo)
class GUI:
    def __init__(self):
        # Initialise GUI
        self.top = tk.Tk()
        self.top.geometry('1280x720')
        self.top.title('VEHICLE CLASSIFICATION')
        self.top.configure(background='#FFFFFF')
        self.label = Label(self.top, background='#FFFFFF', font=('arial', 15, 'bold'))
        self.sign_image = Label(self.top)

        self.upload = Button(self.top, text="Upload an image", command=self.upload_image, padx=12, pady=5)
        self.upload.configure(background='blue', foreground='white', font=('arial', 20, 'bold'))
        self.upload.pack(side=BOTTOM, pady=40)
        

        self.btnClose = tk.Button(self.top, text="CLOSE", font=("Cambria", 20,'bold'),bg='red',fg='white',
                                      command=lambda: self.quitProgram(self.top)) #Chức năng nút nhấn
        self.btnClose.place(x=100, y=630)

        self.sign_image.pack(side=BOTTOM, expand=True)
        self.label.pack(side=BOTTOM, expand=True)
        self.heading = Label(self.top, text="VEHICLE CLASSIFICATION", pady=20, font=('arial', 20, 'bold'))
        self.heading.configure(background='#FFFFFF', foreground='#B20000')
        self.heading.pack()

        # Ảnh trong giao diện 
        anh=Image.open("poster.png")
        # Chỉnh kích thước và vị trí
        resizeimage=anh.resize((350, 450))
        a = ImageTk.PhotoImage(resizeimage)
        img=tk.Label(image=a)
        img.place(x=2,y=100)

        self.top.mainloop()

    def quitProgram(self, window):
        self.top.destroy()

    def classify(self, file_path):
        image = Image.open(file_path)
        image = image.resize((64, 64))
        image = img_to_array(image)
        test_image = np.expand_dims(image, axis=0)
        result = (model.predict(test_image) > 0.5).astype("int32")
        x = 0
        c = 0
        i = 0
        while i < 3:
            if result[0][i] >= x:
                x = result[0][i]
                c = i
            i += 1
        if x <= 0 and c >= 2:
            c = 3
        if c == 0:
            prediction = 'BIKE (Move into lane 1)'
        elif c == 1:
            prediction = 'CAR (Move into lane 2)'
        elif c == 2:
            prediction = 'CONTAINER (Move into lane 3)'

        self.label.configure(background="yellow",foreground='black', text=prediction, font=('arial', 24, 'bold'))

    def show_classify_button(self, file_path):
        classify_b = Button(self.top, text="Classify Image", command=lambda: self.classify(file_path), padx=12, pady=5)
        classify_b.configure(background='green', foreground='white', font=('arial', 20, 'bold'))
        classify_b.place(relx=0.75, rely=0.85)

    def upload_image(self):
        try:
            file_path = filedialog.askopenfilename()
            uploaded = Image.open(file_path)
            uploaded.thumbnail(((self.top.winfo_width() / 2.25), (self.top.winfo_height() / 2.25)))
            im = ImageTk.PhotoImage(uploaded)
            self.sign_image.configure(image=im)
            self.sign_image.image = im
            self.label.configure(text='')
            self.show_classify_button(file_path)
        except:
            pass

mainObj = GUI()