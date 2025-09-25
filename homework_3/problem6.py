import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

def normalize_img(img):
    img = img - np.min(img)
    if np.max(img) != 0:
        img = img / np.max(img) * 255
    return img.astype(np.uint8)

def problem6(img):
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)

    real = np.real(dft_shift)
    imag = np.imag(dft_shift)
    magnitude = np.abs(dft_shift)
    phase = np.angle(dft_shift)

    # Chuẩn hóa 
    real_n = normalize_img(real)
    imag_n = normalize_img(imag)
    mag_n = normalize_img(np.log(1 + magnitude))
    phase_n = normalize_img(phase)


    plt.figure(figsize=(10,8))
    plt.subplot(2,3,1), plt.imshow(img, cmap='gray'), plt.title("Original"), plt.axis("off")
    plt.subplot(2,3,2), plt.imshow(real_n, cmap='gray'), plt.title("Real"), plt.axis("off")
    plt.subplot(2,3,3), plt.imshow(imag_n, cmap='gray'), plt.title("Imag"), plt.axis("off")
    plt.subplot(2,3,5), plt.imshow(mag_n, cmap='gray'), plt.title("Magnitude (log)"), plt.axis("off")
    plt.subplot(2,3,6), plt.imshow(phase_n, cmap='gray'), plt.title("Phase"), plt.axis("off")
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

    problem6(img)

if __name__ == "__main__":
    main()
