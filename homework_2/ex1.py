import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np



def thresholding(img: np.uint8) -> tuple[np.uint8, int]:
    # T = round(img.mean())
    T = 95
    return [np.where(img > T, 255, 0).astype(np.uint8), T]

def approximateContourImageGeneration(img: np.uint8) -> np.uint8:
    rows, cols = img.shape
    contour = np.zeros_like(img, dtype=np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if img[i, j] == 255:
                neighbors = img[i - 1: i + 2, j - 1 : j + 2]
                if np.any(neighbors == 0):
                    contour[i, j] = 255
    return contour


if __name__ == "__main__":
    rows, cols = 256, 256
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--url", type=str, default="Mammogrambin.sec", help="Path to input image")
    args = parser.parse_args()

    url = args.url
    img = np.fromfile(url, dtype=np.uint8).reshape((rows, cols))

    plt.figure(figsize=(8, 8))

    plt.subplot(3, 2, 1)
    plt.title("Original img")
    plt.axis("off")
    plt.imshow(img, cmap="gray")
    
    new_img, T = thresholding(img)
    plt.subplot(3, 2, 2)
    plt.title(f"T: {T}")
    plt.axis("off")    
    plt.imshow(new_img, cmap="gray")

    contour = approximateContourImageGeneration(new_img)
    plt.subplot(3, 2, 3)
    plt.title("contour")
    plt.axis("off")
    plt.imshow(contour, cmap="gray")

    plt.tight_layout()
    plt.show()