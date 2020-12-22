import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

h =  np.array([0, 3, 6]) # wysokosc w metrach
ro = np.array([1.225, 0.905, 0.652]) # gestosc w kg/m^3

f = interp1d(h, ro, kind='quadratic')

plt.plot(h, ro, 'o')

hnew = np.arange(0.0, 6.0, 0.01)

plt.plot(hnew, f(hnew))
plt.show()