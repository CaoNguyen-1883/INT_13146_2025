import argparse
import cv2
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--url", type=str, default="circles.png", help="Path to input image")
    args = parser.parse_args()

    url = args.url
    img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)

    _, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

    kernal30 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 30))
    kernal70 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (70, 70))
    kernal96 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (96, 96))

    erosion30 = cv2.erode(binary, kernal30)
    erosion70 = cv2.erode(binary, kernal70)
    erosion96 = cv2.erode(binary, kernal96)

    plt.subplot(1,4,1)
    plt.imshow(binary, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1,4,2)
    plt.imshow(erosion30, cmap="gray")
    plt.title("erosion30")
    plt.axis("off")

    plt.subplot(1,4,3)
    plt.imshow(erosion70, cmap="gray")
    plt.title("erosion70")
    plt.axis("off")

    plt.subplot(1,4,4)
    plt.imshow(erosion96, cmap="gray")
    plt.title("erosion96")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":   
    main()