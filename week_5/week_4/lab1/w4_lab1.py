from scipy.io import loadmat
import matplotlib.pyplot as plt

data = loadmat("visibleSpectrum.mat")
CMFs = data['CMFs']

wavelength = CMFs[:,0]  # bước sóng
x_bar = CMFs[:,1]
y_bar = CMFs[:,2]
z_bar = CMFs[:,3]

# Vẽ 3 đường
plt.figure(figsize=(8,5))
plt.plot(wavelength, x_bar, 'r', label='r')
plt.plot(wavelength, y_bar, 'g', label='g')
plt.plot(wavelength, z_bar, 'b', label='b')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)  
plt.show()