import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

# g(x,y)=a⋅(f(x,y))**γ

# Đọc ảnh grayscale
img = cv2.imread("demo_2.png", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

gamma = 1.5   # chỉnh gamma

if len(sys.argv) > 1:
    gamma = float(sys.argv[1])

# chuẩn bị ảnh kết quả
img_gamma = np.zeros_like(img)

for i in range(rows):
    for j in range(cols):
        # chuẩn hóa về [0,1]
        norm_val = img[i, j] / 255.0
        # gamma correction
        new_val = 255 * (norm_val ** gamma)
        # ép về int và gán lại
        img_gamma[i, j] = int(new_val)

plt.subplot(1,2,1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(img_gamma, cmap="gray")
plt.title(f"Gamma = {gamma}")
plt.axis("off")

plt.show()