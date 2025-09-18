import cv2
import matplotlib.pyplot as plt
import numpy as np

files = ["is1.png", "is2.png"]

images = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in files]

# for file in files:
#     img = cv2.imread(file)
#     if img is None:
#         print(f"Không đọc được ảnh: {fn}")
#         continue
#     if len(images) > 0:
#         img = cv2.resize(img, (images[0].shape[1], images[0].shape[0]))
#     images.append(img)




# subtracted = cv2.absdiff(images[0], images[1])

rows, cols = images[0].shape
subtracted = np.zeros((rows, cols), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        diff = abs(int(images[0][i, j]) - int(images[1][i, j]))
        subtracted[i, j] = diff


equa_image = cv2.equalizeHist(subtracted)


plt.figure(figsize=(12,4))

plt.subplot(1,4,1)
plt.imshow(images[0], cmap="gray")
plt.title("Image 1")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(images[1], cmap="gray")
plt.title("Image 2")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(subtracted, cmap="gray")
plt.title("subtracted")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(equa_image, cmap="gray")
plt.title("Qualize")
plt.axis("off")

plt.show()