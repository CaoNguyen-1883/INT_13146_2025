import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    rows, cols = 256, 256
    parser = argparse.ArgumentParser(description="Locally adaptive thresholding")
    parser.add_argument("--url", type=str, default="ladybin.sec", help="Path to input image")
    args = parser.parse_args()

    url = args.url
    img = np.fromfile(url, dtype=np.uint8).reshape((rows, cols))


    plt.figure(figsize=(8, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.axis("off")
    plt.title("Original img")

    plt.subplot(2, 2, 2)
    plt.title("Original img histogram")
    plt.hist(img.ravel(), bins=256, range=(0, 256), color="black")

    Imin, Imax = img.min(), img.max()
    stretched = ((img - Imin) / (Imax - Imin) * 255).astype(np.uint8)

    plt.subplot(2, 2, 3)
    plt.imshow(stretched, cmap="gray")
    plt.axis("off")
    plt.title("stretched img")

    plt.subplot(2, 2, 4)
    plt.title("stretched img histogram")
    plt.hist(stretched.ravel(), bins=256, range=(0, 256), color="black")

    plt.tight_layout()
    plt.show()