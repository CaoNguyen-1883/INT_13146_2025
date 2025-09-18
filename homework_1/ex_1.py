import numpy as np
import matplotlib.pyplot as plt

rows, cols = 256, 256

# (a) Đọc ảnh từ file .bin
lena = np.fromfile("lenabin.sec", dtype=np.uint8).reshape((rows, cols))
peppers = np.fromfile("peppersbin.sec", dtype=np.uint8).reshape((rows, cols))

# (b) Tạo ảnh J
J = np.zeros((rows, cols), dtype=np.uint8)
J[:, :cols//2] = lena[:, :cols//2]       # nửa trái Lena
J[:, cols//2:] = peppers[:, cols//2:]   # nửa phải Peppers

# (c) Tạo ảnh K (swap)
K = np.zeros_like(J)
K[:, :cols//2] = J[:, cols//2:]
K[:, cols//2:] = J[:, :cols//2]

# (d) Hiển thị kết quả
plt.figure(figsize=(8,8))
plt.subplot(2,2,1), plt.imshow(lena, cmap="gray"), plt.title("Original Lena"), plt.axis("off")
plt.subplot(2,2,2), plt.imshow(peppers, cmap="gray"), plt.title("Original Peppers"), plt.axis("off")
plt.subplot(2,2,3), plt.imshow(J, cmap="gray"), plt.title("Image J"), plt.axis("off")
plt.subplot(2,2,4), plt.imshow(K, cmap="gray"), plt.title("Image K"), plt.axis("off")
plt.tight_layout()
plt.show()