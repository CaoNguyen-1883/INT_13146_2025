import matplotlib.pyplot as plt
import numpy as np
from problem1 import stretch 

def main():
    u0, v0 = 2.0, 2.0
    COLS, ROWS = np.meshgrid(np.arange(8), np.arange(8))
    I2 = 0.5 * np.exp(-1j * 2*np.pi/8 * (u0*COLS + v0*ROWS))

    plt.subplot(1, 2, 1)
    plt.imshow(stretch(np.real(I2)), cmap='gray')
    plt.title("Re[I2]"); plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(stretch(np.imag(I2)), cmap='gray')
    plt.title("Im[I2]"); plt.axis("off")


    Itilde2 = np.fft.fftshift(np.fft.fft2(I2))

    print("Re[DFT(I2)]:")
    print(np.round(np.real(Itilde2), 4))
    print("Im[DFT(I2)]:")
    print(np.round(np.imag(Itilde2), 4))

    plt.show()


if __name__ == "__main__":   
    main()
