import cv2 
import matplotlib.pyplot as plt

img1 = cv2.imread("bay.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("brain.png", cv2.IMREAD_GRAYSCALE)

imgs = [img1, img2]

plt.figure(figsize=(12, 8))

for i, img in enumerate(imgs):
    hist = cv2.calcHist([img], [0], None, [256], [0,256])

    # Hiển thị ảnh
    plt.subplot(2, 2, 2*i + 1)
    plt.imshow(img, cmap='gray')
    plt.axis("off")
    plt.title(f"Image {i+1}")

    # Hiển thị histogram
    plt.subplot(2, 2, 2*i + 2)
    plt.plot(hist, color='black')
    plt.xlabel("Gray level")
    plt.ylabel("#pixels")
    plt.xlim([0, 256])
    plt.title(f"Histogram {i+1}")

plt.tight_layout()
plt.show()