from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

# dane
x = [0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150]
y = [1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741]

# metoda najmniejszych kwadratow
s = np.polyfit(x, y, 2)
m = np.poly1d(s)

xnew = np.arange(-1, 10.5, 0.01)

plt.plot(x, y, '.', xnew, m(xnew))
plt.show()

print("y(10.5) = " + str(m(10.5)))