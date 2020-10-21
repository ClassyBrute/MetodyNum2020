import numpy as np

I = 1

for n in range(2, 21):
    I = np.e - ((n + 1) * I)
    print("n =", n, "wynik = ", I)
