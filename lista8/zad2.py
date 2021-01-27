from numpy import linalg as lin
from scipy.linalg import hilbert

# tworze macierz Hilberta 6x6
A = hilbert(6)

# obliczam wartosci i wektory wlasne macierzy Hilberta
a, b = lin.eigh(A)

print(f"Wartosci wlasne macierzy = {a}")
print(f"Wektory wlasne macierzy = \n{b}")
