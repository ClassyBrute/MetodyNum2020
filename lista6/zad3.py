import numpy as np
import scipy.interpolate as inter
import matplotlib.pyplot as plt

# dane
x = np.array([-2.2, -0.3, 0.8, 1.9])
y = np.array([-15.18, 10.962, 1.92, -2.04])

# dane do wykresu
f = inter.interp1d(x, y, kind="quadratic")
x_new = np.arange(-2.2, 1.9, 0.01)
y_new = f(x_new)

# wyrysowanie danych na wykresie
plt.plot(x, y, "o", x_new, y_new, "-")
plt.show()

# wielomian
dane = inter.lagrange(x, y)

# wyliczanie pierwszej i drugiej pochodnej
poch_f1 = np.polyder(dane)
poch_f2 = np.polyder(dane, 2)

print(f"Pierwsza pochodna f'(0) = {poch_f1(0.0)} \nDruga pochodna f''(0) = {poch_f2(0.0)}")