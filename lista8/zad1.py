import numpy as np
from numpy import linalg as lin

# tworze macierz podana w poleceniu
A = np.array([[-1, 4, 1],
              [-1, -2, -5],
              [5, 4, 3]])

# obliczam wartosci i wektory wlasne macierzy
a, b = lin.eig(A)

print(f"Wartosci wlasne macierzy = {a}")
print(f"Wektory wlasne macierzy = \n{b}")