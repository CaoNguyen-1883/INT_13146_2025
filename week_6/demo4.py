import argparse
import matplotlib.pyplot as plt
import cv2

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--url", type=str, default="fence.jpg", help="Path to input image")
    args = parser.parse_args()

    url = args.url
    img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)

    # _, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    T, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (107, 107))
    newImg = cv2.erode(otsu, kernal)

    plt.figure(figsize=(16, 4))

    plt.subplot(1,3,1)
    plt.imshow(img, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(otsu, cmap="gray")
    plt.title(f"otsu, T = {T}")
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.imshow(newImg, cmap="gray")
    plt.title("newImg")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":   
    main()