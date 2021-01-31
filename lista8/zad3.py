import numpy as np
from scipy.linalg import eigh_tridiagonal

n = 10
n1 = 100

# dla n = 10
d = 2*np.ones(n)
nd = -1*np.ones(n-1)

# dla n = 100
d1 = 2*np.ones(n1)
nd1 = -1*np.ones(n1-1)

wart, wekt = eigh_tridiagonal(d, nd)
print(f"Macierz n = {n}")
print(f"Trzy namniejsze wartosci wlasne = {wart[:3]}")
print(f"Trzy najmniejsze wektory wlasne = {wekt[:, :3]}")

wart1, wekt1 = eigh_tridiagonal(d1, nd1)
print(f"\nMacierz n = {n1}")
print(f"Trzy namniejsze wartosci wlasne = {wart1[:3]}")
print(f"Trzy najmniejsze wektory wlasne = {wekt1[:, :3]}")
