import argparse
import numpy as np
import matplotlib.pyplot as plt

def read_bin(path, size=256):
    return np.fromfile(path, dtype=np.uint8).reshape((size, size))

def build_template():
    T = np.zeros((47, 15), dtype=np.uint8)
    T[10:16, :] = 255                # thanh ngang
    T[16:37, 6:10] = 255             # thanh dọc
    return T

def stretch(img):
    imin, imax = img.min(), img.max()
    return ((img - imin) * 255 / (imax - imin)).astype(np.uint8)

def match_template(img, T):
    r, c = T.shape
    ro2, co2 = r // 2, c // 2
    J1 = np.zeros_like(img, dtype=np.float32)

    for i in range(ro2, img.shape[0] - ro2):
        for j in range(co2, img.shape[1] - co2):
            W = img[i-ro2:i+ro2+1, j-co2:j+co2+1]
            if W.shape == T.shape:
                J1[i, j] = np.sum(W == T)
    return J1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="actontBinbin.sec")
    args = parser.parse_args()

    img = read_bin(args.url)
    T = build_template()
    J1 = match_template(img, T)
    J1s = stretch(J1)

    # threshold theo 2 giá trị cao nhất
    thresh = np.sort(J1.ravel())[-2]
    J2 = (J1 >= thresh).astype(np.uint8) * 255

    # hiển thị
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap="gray", origin="upper")
    plt.title("Original")

    plt.subplot(1, 3, 2)
    plt.imshow(J1s, cmap="gray", origin="upper")
    plt.title("J1 (M2)")

    plt.subplot(1, 3, 3)
    plt.imshow(J2, cmap="gray", origin="upper")
    plt.title(f"J2 (τ={thresh:.0f})")

    plt.show()

if __name__ == "__main__":
    main()
