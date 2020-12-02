import numpy as np
from scipy import optimize

def f(x):
    return [x[0] + np.exp(-1*x[0]) + x[1]**3, x[0]**2 + 2*x[0]*x[1] - x[1]**2 + np.tan(x[0])]


xy = [np.array([-1.2, -1.2]), np.array([-0.7, -0.7]), np.array([1.2, 1.2])]     # zgadujemy wyniki
result = []

for i in xy:
    x1 = optimize.root(f, i)    # podajemy funkcję, a potem initial guess

    if(x1.success):
        if(x1.x[0]**2 + x1.x[1]**2 <= 4):   # sprawdzamy czy leży w okręgu
            result.append(x1.x)

print(result)