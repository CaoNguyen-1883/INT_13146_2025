import argparse
import numpy as np
import matplotlib.pyplot as plt

def read_bin(path, size=256):
    return np.fromfile(path, dtype=np.uint8).reshape((size, size))

def hist_eq(img):
    hist, _ = np.histogram(img.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()
    cdf_norm = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    cdf_norm = cdf_norm.astype(np.uint8)
    return cdf_norm[img]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="johnnybin.sec")
    args = parser.parse_args()

    img = read_bin(args.url)

    hist_orig, _ = np.histogram(img.flatten(), bins=256, range=[0, 256])
    img_eq = hist_eq(img)
    hist_eqv, _ = np.histogram(img_eq.flatten(), bins=256, range=[0, 256])

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap="gray", origin="upper")
    plt.title("Original Image")

    plt.subplot(2, 2, 2)
    plt.bar(range(256), hist_orig, width=1, color="black")
    plt.title("Original Histogram")

    plt.subplot(2, 2, 3)
    plt.imshow(img_eq, cmap="gray", origin="upper")
    plt.title("Equalized Image")

    plt.subplot(2, 2, 4)
    plt.bar(range(256), hist_eqv, width=1, color="black")
    plt.title("Equalized Histogram")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
