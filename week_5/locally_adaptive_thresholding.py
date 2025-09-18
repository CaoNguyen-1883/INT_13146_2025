import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Locally adaptive thresholding")
    parser.add_argument("--url", type=str, default="paper.png", help="Path to input image")
    args = parser.parse_args()

    url = args.url

    img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)

    block_size = 11
    C = 2

    pad = block_size // 2
    padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REFLECT)

    adaptive_result = np.zeros_like(img)




    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Lấy block lân cận
            block = padded[i:i+block_size, j:j+block_size]
            T, _ = cv2.threshold(block, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # So sánh pixel gốc với ngưỡng Otsu
            adaptive_result[i, j] = 255 if img[i, j] > T else 0

    opencv_image = cv2.adaptiveThreshold(
        img, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        block_size, C
    )
    # Hiển thị kết quả
    plt.figure(figsize=(12,6))

    plt.subplot(1,3,1)
    plt.title(f"Original image: {url}")
    plt.imshow(img, cmap="gray")

    plt.subplot(1,3,2)
    plt.title(f"Manual Adaptive, T = {T}")
    plt.imshow(adaptive_result, cmap="gray")

    plt.subplot(1,3,3)
    plt.title("Opencv Adaptive")
    plt.imshow(opencv_image, cmap="gray")

    plt.show()