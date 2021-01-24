import numpy as np
import scipy.integrate as integ

# podana funkcja
def f(x):
    return np.cos(2*np.cos(x)**-1)

# dla 3 węzłów
x3 = np.linspace(-1, 1, 3)
y3 = []
y3.append(f(x3))
wezly3 = integ.simps(y3, x3)

# dla 5 węzłów
x5 = np.linspace(-1, 1, 5)
y5 = []
y5.append(f(x5))
wezly5 = integ.simps(y5, x5)

# dla 7 węzłów
x7 = np.linspace(-1, 1, 7)
y7 = []
y7.append(f(x7))
wezly7 = integ.simps(y7, x7)

# większa liczba węzłów przybliża nas do prawidłowego wyniku
print(f"Wynik całkowania dla 3 węzłów = {wezly3[0]}\n Wynik całkowania dla 5 węzłów = {wezly5[0]}\n Wynik całkowania dla 7 węzłów = {wezly7[0]}")
