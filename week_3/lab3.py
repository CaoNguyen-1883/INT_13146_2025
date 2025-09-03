import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("moon.png", cv2.IMREAD_GRAYSCALE)


clip_limits = [0, 0.1, 0.4, 0.7] 
results = {}


he = cv2.equalizeHist(img)
results["no clipping"] = he


for cl in clip_limits[1:]:
    clahe = cv2.createCLAHE(clipLimit=cl*5, tileGridSize=(8,8))  
    res = clahe.apply(img)
    results[f"clip {cl}"] = res


plt.figure(figsize=(14, 8))


plt.subplot(2, 2, 1)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist, color='blue')
plt.title("Input Histogram")
plt.xlabel("Gray level")
plt.ylabel("#pixels")


plt.subplot(2, 2, 2)
for label, res in results.items():
    mapping = [np.mean(res[img == i]) if np.any(img == i) else 0 for i in range(256)]
    plt.plot(mapping, label=label)
plt.title("Mapping Function")
plt.xlabel("Input gray level")
plt.ylabel("Output gray level")
plt.legend()

for idx, (label, res) in enumerate(results.items()):
    plt.subplot(2, len(results), len(results)+idx+1)
    plt.imshow(res, cmap='gray')
    plt.title(label)
    plt.axis("off")

plt.tight_layout()
plt.show()

