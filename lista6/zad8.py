from scipy.integrate import dblquad
import numpy as np

# dana calka
def f(y, x):
    result = np.sin(np.pi * x) * np.sin(np.pi * (y - x))
    return result

wynik = dblquad(f, 0, 1, lambda x : 0, lambda x : x)

print(f"Wynik = {wynik[0]}\nDokladnosc = {wynik[1]}")