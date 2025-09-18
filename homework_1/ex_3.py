import cv2
import matplotlib.pyplot as plt

# (b) Đọc ảnh màu
J1 = cv2.imread("lena512color.jpg")
# OpenCV đọc theo BGR, cần đổi sang RGB để hiển thị đúng với matplotlib
J1 = cv2.cvtColor(J1, cv2.COLOR_BGR2RGB)

# Hiển thị ảnh gốc
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.imshow(J1)
plt.title("Original lena512color.jpg")
plt.axis("off")
plt.savefig("P3J1.eps")   # xuất EPS cho báo cáo

# (c) Tạo J2 bằng cách tráo kênh màu
J2 = J1.copy()
J2[:,:,0] = J1[:,:,2]   # Red <- Blue
J2[:,:,1] = J1[:,:,0]   # Green <- Red
J2[:,:,2] = J1[:,:,1]   # Blue <- Green

# Hiển thị J2
plt.subplot(1,2,2)
plt.imshow(J2)
plt.title("Color Bands Switched")
plt.axis("off")
plt.savefig("P3J2.eps")   # xuất EPS cho báo cáo
plt.show()

# Lưu J2 ra JPEG
J2_bgr = cv2.cvtColor(J2, cv2.COLOR_RGB2BGR)  # đổi lại BGR cho OpenCV ghi file
cv2.imwrite("LenaColorSwitch.jpg", J2_bgr)
