import numpy as np
import scipy.interpolate as inter
import matplotlib.pyplot as plt

# dane
x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
y = np.array([0.0, 0.078348, 0.13891, 0.192916, 0.244981])

# dane do wykresu
f = inter.interp1d(x, y, kind="quadratic")
x_new = np.arange(0.0, 0.4, 0.01)
y_new = f(x_new)

# wyrysowanie danych na wykresie
plt.plot(x, y, "o", x_new, y_new, "-")
plt.show()

dane = inter.lagrange(x, y) # wielomian
pochodna = np.polyder(dane) # pochodna wielomianu

print(f"Pochodna w x=0.2  = {pochodna(0.2)}")