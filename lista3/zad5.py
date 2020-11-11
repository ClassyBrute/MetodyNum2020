import numpy as np
from scipy.linalg import hilbert

def zadanie(n):
    h = hilbert(n)

    norm = np.linalg.norm(h)
    cond = np.linalg.cond(h)

    print("Dla macierzy Hilberta " + str(n) + "x" + str(n))
    print("Norma " + " = " + str(norm))
    print("Wskaznik uwarunkowania " + " = " + str(cond))

# norma i wskaznik uwarunkowania dla macierzy Hilberta 5x5
zadanie(5)

# norma i wskaznik uwarunkowania dla macierzy Hilberta 10x10
zadanie(10)

# norma i wskaznik uwarunkowania dla macierzy Hilberta 20x20
zadanie(20)