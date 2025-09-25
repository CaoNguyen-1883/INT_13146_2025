import matplotlib.pyplot as plt
import numpy as np
from problem1 import stretch 

def main():
    COLS, ROWS = np.meshgrid(np.arange(8), np.arange(8))
    u1, v1 = 1.5, 1.5
    I5 = np.cos(2*np.pi/8 * (u1*COLS + v1*ROWS))

    plt.figure()
    plt.imshow(stretch(I5), cmap='gray')
    plt.title("I5"); plt.axis("off")

    Itilde5 = np.fft.fftshift(np.fft.fft2(I5))

    print("Re[DFT(I5)]:")
    print(np.round(np.real(Itilde5), 4))
    print("Im[DFT(I5)]:")
    print(np.round(np.imag(Itilde5), 4))
    plt.show()


if __name__ == "__main__":   
    main()
