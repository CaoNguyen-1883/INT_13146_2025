import cv2
import matplotlib.pyplot as plt
import numpy as np


image = cv2.imread("demo_1.png", cv2.IMREAD_GRAYSCALE)

img_quant = image



for i, bit in enumerate([1, 2, 3, 4, 5, 8]):

    levels = 2**bit #init gray level

    step = 256 // levels #step of gray level

    img_quant = image.copy()

    for j in range(img_quant.shape[0]):      
        for k in range(img_quant.shape[1]): 
            img_quant[j][k] = (img_quant[j][k] // step) * step

    i = i + 1


    plt.subplot(2, 3, i)
    plt.imshow(img_quant, cmap="gray")
    plt.title(f"{bit} bits ({levels} levels)")
    plt.axis("off")


plt.tight_layout()
plt.show()