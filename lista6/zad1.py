import numpy as np
import scipy.misc as sp

# funkcja do obliczenia
def f(x):
    result = np.log(np.tanh(x/(x**2 + 1)))
    return result

x = 0.2 # w ktorym punkcie obliczyc pochodne
dx = 0.0001 # rozstaw

# obliczanie pierwszej, drugiej i trzeciej pochodnej
poch_f1 = sp.derivative(f, x, dx, order=7)
poch_f2 = sp.derivative(f, x, dx, 2, order=7)
poch_f3 = sp.derivative(f, x, dx, 3, order=7)

print(f"Pierwsza pochodna = {poch_f1}, Druga pochodna = {poch_f2}, Trzecia pochodna = {poch_f3}")