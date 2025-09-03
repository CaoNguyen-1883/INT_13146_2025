import cv2
import numpy as np
from tkinter import Tk, Button, Scale, HORIZONTAL, filedialog, Label
from PIL import Image, ImageTk

root = Tk()
root.title("Brightness Adjustment with Gamma Correction")
root.geometry("1100x800")

img_gray = None
img_label = Label(root)
img_label.pack()

def update(_=None):
    global img_gray
    if img_gray is None:
        return

    # Lấy hệ số a từ slider brightness (%)
    a = scale_a.get() / 100.0  

    # Lấy gamma từ slider gamma
    gamma = scale_gamma.get() / 100.0  

    # Tính toán theo công thức f[x,y] -> (a*f[x,y])^γ
    adjusted = np.clip((a * img_gray.astype(np.float32)) ** gamma, 0, 255).astype(np.uint8)

    # Hiển thị ảnh đã chỉnh
    imgtk = ImageTk.PhotoImage(image=Image.fromarray(adjusted).resize((800, 600)))
    img_label.config(image=imgtk)
    img_label.image = imgtk

def choose_image():
    global img_gray
    file_path = filedialog.askopenfilename(title="Chọn ảnh", 
                                           filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        update()

# Nút chọn ảnh
btn = Button(root, text="Chọn ảnh", command=choose_image, font=("Arial", 14))
btn.pack(pady=10)

# Slider brightness % (50% – 200%)
scale_a = Scale(root, from_=50, to=200, orient=HORIZONTAL, 
                label="Brightness scale a (% so với ảnh gốc)", 
                command=update, length=500, font=("Arial", 12))
scale_a.set(100)  # mặc định = 100% (ảnh gốc)
scale_a.pack(pady=20)

# Slider gamma (0.1 – 3.0, scale theo % để dễ dùng)
scale_gamma = Scale(root, from_=10, to=300, orient=HORIZONTAL, 
                    label="Gamma (γ)", 
                    command=update, length=500, font=("Arial", 12))
scale_gamma.set(100)  # mặc định = 1.0
scale_gamma.pack(pady=20)

root.mainloop()
