import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0, 1.5, 0.001)
y1 = np.cos(x1) - (3 * np.sin(np.tan(x1) - 1))
liczba = 0
os_x = np.zeros(1500)

# rysuje wykres i oś x
plt.plot(y1)
plt.plot(os_x)
plt.show()
