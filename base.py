import argparse
import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--url", type=str, default="peter.png", help="Path to input image")
    args = parser.parse_args()

    url = args.url
    img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)

    _, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)


if __name__ == "__main__":   
    main()



def stretch(img):
    """Scale array to [0,255] uint8"""
    img_min, img_max = img.min(), img.max()
    if img_max - img_min == 0:
        return np.zeros_like(img, dtype=np.uint8)
    return np.uint8(255 * (img - img_min) / (img_max - img_min))
