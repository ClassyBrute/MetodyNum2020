from scipy import integrate
import numpy as np

# dana calka
def f(x):
    result = (np.cos(x) - np.exp(x)) / np.sin(x)
    return result

wynik = integrate.quadrature(f, -0.9999999999, 1.0, tol=1.0e-11)

print(f"Wynik = {wynik[0]}\nDokladnosc = {wynik[1]}")