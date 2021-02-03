import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def funkcja(t, y):
    return np.sin(t * y)

y0 = [2, 2.5, 3, 3.5]

for i in y0:
    result = solve_ivp(funkcja, [0, 6], [i], atol=1e-12, rtol=1e-9)

    print(result)
    plt.plot(result.t, result.y[0])

plt.legend(['y0=2', 'y0=2.5', 'y0=3', 'y0=3.5'])
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.show()