import cv2 
import matplotlib.pyplot as plt
import numpy as np
import argparse

def threshold(img: cv2.typing.MatLike, T: int, isReverse: bool = False) -> cv2.typing.MatLike:
    if isReverse:
        return np.where(img <= T, 255, 0).astype(np.uint8)
    return np.where(img >= T, 255, 0).astype(np.uint8)

if __name__ == "__main__":   
    parser = argparse.ArgumentParser(description="Gray level thresholding")
    parser.add_argument("--url", type=str, default="peter.png", help="Path to input image")
    parser.add_argument("--T", type=int, default=128, help="Threshold value")
    parser.add_argument("--R", type=bool, default=False, help="Threshold value")
    args = parser.parse_args()

    url = args.url
    T = args.T
    isReverse = args.R
        
    image = cv2.imread(url, cv2.IMREAD_GRAYSCALE)

    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Original image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(threshold(image, T, isReverse), cmap="gray")
    plt.title(f"Thresholding = {T}")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
