from scipy import special
import numpy as np

# dana calka
def f(x):
    result = np.log(x) / (x**2 - 2*x + 2)
    return result

# zakres calkowania
a = 1
b = np.pi

# dla 2 wezlow
x = special.roots_legendre(2, mu=True)
wynik = 0

for i in range(len(x)):
    wynik += ((b - a) / 2) * x[i] * f((b + a) / 2 + ((b - a) / 2 * x[i]))

print(f"Wynik dla 2 wezlow = {wynik[1]}")

# dla 4 wezlow
x = special.roots_legendre(4, mu=True)
wynik = 0

for i in range(len(x)):
    wynik += ((b - a) / 2) * x[i] * f((b + a) / 2 + ((b - a) / 2 * x[i]))

print(f"Wynik dla 4 wezlow = {wynik[3]}")


# https://chem.pg.edu.pl/documents/175260/14212622/smo_sem_017.pdf