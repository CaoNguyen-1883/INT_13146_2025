import cv2
import matplotlib.pyplot as plt

# Đọc ảnh grayscale
J1 = cv2.imread("lenagray.jpg", cv2.IMREAD_GRAYSCALE)

# Hiển thị ảnh gốc
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(J1, cmap="gray")
plt.title("Original lenagray.jpg")
plt.axis("off")

# Tạo ảnh âm bản
J2 = 255 - J1

# Hiển thị ảnh âm bản
plt.subplot(1,2,2)
plt.imshow(J2, cmap="gray")
plt.title("Photographic Negative")
plt.axis("off")

plt.tight_layout()
plt.show()

# Lưu ảnh âm bản
cv2.imwrite("LenaNegative.jpg", J2)
