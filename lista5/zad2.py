import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.optimize import bisect
from scipy.misc import derivative

x = np.arange(1, 3.1, 0.25)
y = np.array([-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334])

f = interp1d(x, y, kind='cubic')

xnew = np.arange(1, 3, 0.01)
ynew = f(xnew)

plt.plot(x, y, 'o', xnew, ynew, '-')

# przedzialy pierwiastkow odczytane z wykresu
roots0 = bisect(f, 1.20, 1.3)
roots1 = bisect(f, 2, 2.3)
roots2 = bisect(f, 2.7, 3)
print("Pierwiastki: ", roots0, roots1, roots2)

# pochodna y'(2.1)
df_0 = np.poly1d(ynew)
df_1 = derivative(df_0, 2.1)

print("y'(2.1) = ", df_1)
plt.show()
