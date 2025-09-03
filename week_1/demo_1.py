import cv2
import numpy as np
from tkinter import Tk, Button, Scale, HORIZONTAL, filedialog, Label
from PIL import Image, ImageTk

# Khởi tạo cửa sổ chính
root = Tk()
root.title("Gray Levels Quantization by Bit Depth")
root.geometry("1000x700")

img_gray = None
img_label = Label(root)
img_label.pack()

def update(bits):
    global img_gray
    if img_gray is None:
        return
    bits = int(bits)
    levels = 2 ** bits  # số mức xám theo bit
    step = 256 // levels
    quantized = (img_gray // step) * step

    imgtk = ImageTk.PhotoImage(image=Image.fromarray(quantized).resize((800, 600)))
    img_label.config(image=imgtk)
    img_label.image = imgtk

def choose_image():
    global img_gray
    file_path = filedialog.askopenfilename(title="Chọn ảnh", 
                                           filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        update(scale.get())

# Nút chọn ảnh
btn = Button(root, text="Chọn ảnh", command=choose_image, font=("Arial", 14))
btn.pack(pady=10)

# Slider chọn số bit (1 → 8)
scale = Scale(root, from_=1, to=8, orient=HORIZONTAL, label="Bit Depth", 
              command=update, length=500, font=("Arial", 12))
scale.set(8)  # mặc định là 8 bit = ảnh gốc
scale.pack(pady=20)

root.mainloop()
