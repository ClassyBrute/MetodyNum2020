from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

# dane
x = [1, 2.5, 3.5, 4, 1.1, 1.8, 2.2, 3.7]
y = [6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828]

# dopasowywanie funkcji
f = interpolate.interp1d(x, y, kind = "quadratic")

xnew = np.arange(1, 4, 0.001)
ynew = f(xnew)

# dopasowywanie prostej
liniowe = np.polyfit(x, y, 1)
liniowe_y = np.poly1d(liniowe)(x)

plt.plot(x, y, 'o', xnew, ynew, '-')
plt.plot(x, liniowe_y)
plt.show()