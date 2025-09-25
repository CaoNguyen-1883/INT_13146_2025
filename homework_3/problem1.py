import matplotlib.pyplot as plt
import numpy as np

def stretch(img):
    """Scale array to [0,255] uint8"""
    img_min, img_max = img.min(), img.max()
    if img_max - img_min == 0:
        return np.zeros_like(img, dtype=np.uint8)
    return np.uint8(255 * (img - img_min) / (img_max - img_min))

def main():
    u0, v0 = 2.0, 2.0
    COLS, ROWS = np.meshgrid(np.arange(8), np.arange(8))
    I1 = 0.5 * np.exp(1j * 2*np.pi/8 * (u0*COLS + v0*ROWS))

    # Stretch real + imag
    I1R = stretch(np.real(I1))
    I1I = stretch(np.imag(I1))

    plt.subplot(1, 2, 1)
    plt.imshow(I1R, cmap='gray')
    plt.title("Re[I1]"); plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(I1I, cmap='gray')
    plt.title("Im[I1]"); plt.axis("off")



    # DFT
    Itilde1 = np.fft.fftshift(np.fft.fft2(I1))

    print("Re[DFT(I1)]:")
    print(np.round(np.real(Itilde1), 4))
    print("Im[DFT(I1)]:")
    print(np.round(np.imag(Itilde1), 4))
    plt.show()


if __name__ == "__main__":   
    main()
