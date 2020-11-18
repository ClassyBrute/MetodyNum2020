from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2 * x**4 + 24 * x**3 + 61 * x**2 - 16 * x + 1

# wyrysowuje wykres funkcji aby wiedziec w jakich
# przedzialach nalezy sprawdzac wartosc miejsc zerowych
wykr1 = []
y = np.arange(-10, 5, 0.5)

for x in np.arange(-10, 5, 0.5):
    wykr = 2 * (x**4) + 24 * (x**3) + 61 * (x**2) - 16 * x + 1
    wykr1.append(wykr)

plt.plot(y, wykr1)
plt.grid(True)
plt.show()

# dla widocznych na wykresie okolic miejsc zerowych uzywam funkcji ridder
result1 = optimize.ridder(f, -9, -7)
result2 = optimize.ridder(f, -5, -3)
result3 = optimize.ridder(f, 0, 0.122)
result4 = optimize.ridder(f, 0.122, 0.124)

print("Pierwsze miejsce zerowe = " + str(result1))
print("Drugie miejsce zerowe = " + str(result2))
print("Trzecie miejsce zerowe = " + str(result3))
print("Czwarte miejsce zerowe = " + str(result4))