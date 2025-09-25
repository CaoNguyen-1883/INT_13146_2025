import matplotlib.pyplot as plt
import numpy as np
from problem1 import stretch 

def main():
    u0, v0 = 2.0, 2.0
    COLS, ROWS = np.meshgrid(np.arange(8), np.arange(8))
    I3 = np.cos(2*np.pi/8 * (u0*COLS + v0*ROWS))

    plt.figure()
    plt.imshow(stretch(I3), cmap='gray')
    plt.title("I3"); plt.axis("off")

    Itilde3 = np.fft.fftshift(np.fft.fft2(I3))

    print("Re[DFT(I3)]:")
    print(np.round(np.real(Itilde3), 4))
    print("Im[DFT(I3)]:")
    print(np.round(np.imag(Itilde3), 4))

    plt.show()


if __name__ == "__main__":   
    main()
