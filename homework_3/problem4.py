import matplotlib.pyplot as plt
import numpy as np
from problem1 import stretch 

def main():
    u0, v0 = 2.0, 2.0
    COLS, ROWS = np.meshgrid(np.arange(8), np.arange(8))
    I4 = np.sin(2*np.pi/8 * (u0*COLS + v0*ROWS))

    plt.figure()
    plt.imshow(stretch(I4), cmap='gray')
    plt.title("I4"); plt.axis("off")

    Itilde4 = np.fft.fftshift(np.fft.fft2(I4))

    print("Re[DFT(I4)]:")
    print(np.round(np.real(Itilde4), 4))
    print("Im[DFT(I4)]:")
    print(np.round(np.imag(Itilde4), 4))

    plt.show()


if __name__ == "__main__":   
    main()
