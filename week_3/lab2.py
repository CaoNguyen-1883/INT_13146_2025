import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("bay.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("brain.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("moon.png", cv2.IMREAD_GRAYSCALE)

images = [img1, img2, img3]

plt.figure(figsize=(15,12))

for i, img in enumerate(images):

    hist_orig = cv2.calcHist([img], [0], None, [256], [0, 256])
    
    # Equalization
    img_eq = cv2.equalizeHist(img)
    hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])
    
    plt.subplot(3,3,i*3+1)
    plt.imshow(img, cmap='gray')
    plt.axis("off")
    
    # Histogram 
    plt.subplot(3,3,i*3+2)
    plt.plot(hist_orig, color='black')
    plt.xlabel("Gray level")
    plt.ylabel("#pixels")
    plt.xlim([0,256])       
    
    # Histogram equalized
    plt.subplot(3,3,i*3+3)
    plt.plot(hist_eq, color='black')
    plt.xlabel("Gray level")
    plt.ylabel("#pixels")
    plt.xlim([0,256])

plt.tight_layout()
plt.show()
