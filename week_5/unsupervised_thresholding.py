import cv2
import matplotlib.pyplot as plt
import argparse
import numpy as np
from gray_level_thresholding import threshold




def otsu_threshold(img):
    # Histogram
    hist, _ = np.histogram(img, bins=256, range=(0, 256))
    total = img.size

    # Normalize histogram to get probabilities
    prob = hist / total

    # Cumulative sums
    omega1 = np.cumsum(prob)
    omega2 = np.cumsum(prob[::-1])[::-1]
    print(omega1, omega2)
    # Cumulative means
    bin_mids = np.arange(256)
    mu1 = np.cumsum(prob * bin_mids) / omega1
    mu2 = (np.cumsum((prob * bin_mids)[::-1]) / omega2[::-1])[::-1]

    # Between-class variance
    sigma_b2 = omega1[:-1] * omega2[1:] * (mu1[:-1] - mu2[1:])**2

    # Best threshold = index with max variance
    T = np.argmax(sigma_b2)
    return T



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Locally adaptive thresholding")
    parser.add_argument("--url", type=str, default="paper.png", help="Path to input image")
    args = parser.parse_args()

    url = args.url
    img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)

    T = otsu_threshold(img)
    new_img = threshold(img, T)

    plt.subplot(1,2,1)
    plt.imshow(img, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(new_img, cmap="gray")
    plt.title(f"T: {T}")
    plt.axis("off")

    plt.show()
