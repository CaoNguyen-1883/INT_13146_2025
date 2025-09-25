import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

def normalize_img(img):
    img = img - np.min(img)
    if np.max(img) != 0:
        img = img / np.max(img) * 255
    return img.astype(np.uint8)

def problem7(img):
    dft = np.fft.fft2(img)

    mag = np.abs(dft)
    J1 = mag * np.exp(1j * 0)
    img_J1 = np.fft.ifft2(J1).real
    JJ1 = np.log(1 + np.abs(J1))

    phase = np.angle(dft)
    J2 = np.exp(1j * phase)
    img_J2 = np.fft.ifft2(J2).real

    JJ1_n = normalize_img(JJ1)
    img_J1_n = normalize_img(img_J1)
    img_J2_n = normalize_img(img_J2)

    plt.figure(figsize=(12,6))
    plt.subplot(1,4,1), plt.imshow(img, cmap="gray"), plt.title("Original"), plt.axis("off")
    plt.subplot(1,4,2), plt.imshow(JJ1_n, cmap="gray"), plt.title("JJ1 log-magnitude"), plt.axis("off")
    plt.subplot(1,4,3), plt.imshow(img_J1_n, cmap="gray"), plt.title("IFFT J1 (no phase)"), plt.axis("off")
    plt.subplot(1,4,4), plt.imshow(img_J2_n, cmap="gray"), plt.title("IFFT J2 (phase only)"), plt.axis("off")
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="camerabin.sec", help="Path to input image (256x256, 8-bit)")
    args = parser.parse_args()

    if args.url.endswith(".sec"):
        img = np.fromfile(args.url, dtype=np.uint8).reshape((256,256))
    else:
        img = cv2.imread(args.url, cv2.IMREAD_GRAYSCALE)

    problem7(img)

if __name__ == "__main__":
    main()
