from scipy.io import loadmat
import matplotlib.pyplot as plt

data = loadmat("coneFundamentals.mat")
cfs = data["coneFundamentals"]

wavelength = cfs[:,0]

x_bar = cfs[:,1]
y_bar = cfs[:,2]
z_bar = cfs[:,3]

plt.figure(figsize=(8,5))
plt.plot(wavelength, x_bar, 'r', label='r')
plt.plot(wavelength, y_bar, 'g', label='g')
plt.plot(wavelength, z_bar, 'b', label='b')
plt.xlabel("nm")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()