import argparse
import cv2
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="bacteria.png", help="Path to input image")
    args = parser.parse_args()

    url = args.url
    img = cv2.imread(url, cv2.IMREAD_GRAYSCALE) 
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    kernel7 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

    dilate3 = cv2.dilate(binary, kernel3, iterations=1)
    dilate7 = cv2.dilate(binary, kernel7, iterations=1)

    plt.subplot(1,3,1)
    plt.imshow(binary, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(dilate3, cmap="gray")
    plt.title("Dilation 3x3")
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.imshow(dilate7, cmap="gray")
    plt.title("Dilation 7x7")
    plt.axis("off")


    plt.tight_layout()
    plt.show()


if __name__ == "__main__":   
  main()