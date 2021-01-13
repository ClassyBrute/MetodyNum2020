import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

Re = np.array([0.2, 2, 20, 200, 2000, 20000])
Cd = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])

dane = CubicSpline(np.log(Re), np.log(Cd))

x = np.array([5, 50, 5000])
y = np.exp(dane(np.log(x)))

x1 = np.arange(0.2, 20000, 1)
y1 = np.exp(dane(np.log(x1)))

plt.plot(Re, Cd, 'o')
plt.plot(x, y, 'ob')
plt.plot(x1, y1)
plt.xscale('log')
plt.yscale('log')
plt.show()
