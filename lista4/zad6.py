import numpy as np
import math
from scipy import optimize

def f(dane):
     x, y = dane
     f1 = math.tan(x) - y - 1           # pierwsza funkcja
     g1 = math.cos(x) - 3 * math.sin(y) # druga funkcja

     return [f1, g1]

result = []

for i in np.arange(0, 1.6, 0.01):
     for j in np.arange(0, 1.6, 0.01):       # iteracja szukająca bliskich wyników
          x1 = optimize.root(f, [i, j])      # podajemy funkcję, a potem initial guess

          if(x1.success):
               if 0 <= round(x1.x[0], 3) <= 1.5:       # sprawdzamy czy znajduje się w przedziale
                    if [round(x1.x[0], 3), round(x1.x[1], 3)] not in result: # sprawdzamy czy wyniki się nie powtarzają
                         result.append([round(x1.x[0], 3), round(x1.x[1], 3)])

print(result)