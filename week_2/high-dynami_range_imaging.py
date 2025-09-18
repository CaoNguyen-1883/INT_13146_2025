import cv2
import matplotlib.pyplot as plt

filenames = ["hdri1.png", "hdri2.png", "hdri3.png", "hdri4.png"]
images = [cv2.imread(fn) for fn in filenames]

# Đọc ảnh và resize về cùng kích thước
images = []
for fn in filenames:
    img = cv2.imread(fn)
    if img is None:
        print(f"Không đọc được ảnh: {fn}")
        continue
    # Resize về cùng size (ví dụ size của ảnh đầu tiên)
    if len(images) > 0:
        img = cv2.resize(img, (images[0].shape[1], images[0].shape[0]))
    images.append(img)

# Exposure Fusion (Mertens et al. 2007)
merge_mertens = cv2.createMergeMertens()
fusion = merge_mertens.process(images)

# Kết quả trả về là float32 trong [0,1] -> chuyển về 8-bit để lưu/hiển thị
fusion_8bit = (fusion * 255).astype("uint8")

# Hiển thị so sánh
plt.figure(figsize=(12,6))
for i, img in enumerate(images, 1):
    plt.subplot(1, len(images)+1, i)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(f"Exposure {i}")
    plt.axis("off")

plt.subplot(1, len(images)+1, len(images)+1)
plt.imshow(cv2.cvtColor(fusion_8bit, cv2.COLOR_BGR2RGB))
plt.title("HDR Fusion")
plt.axis("off")

plt.tight_layout()
plt.show()

# Lưu kết quả
cv2.imwrite("hdr_fusion.jpg", fusion_8bit)