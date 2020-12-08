import numpy as np
import math
from scipy import optimize

g = 9.81 # grawitacja
h = 2    # wysokosc koszykarza
s = 10   # odleglosc od kosza
H = 3    # wysokosc kosza
kat = 45 # kat pod jakim ma wpasc

def f(dane):
    v, kat = dane
    t = 10 / (v * np.cos(kat))     # przekształcone pierwsze równanie

    f1 =  v * np.sin(kat) * t - ((g * t**2) / 2) - 1 # funkcja y
    f2 =  v * (np.sin(kat) + np.cos(kat)) - (g * t)

    return [f1, f2]

result = optimize.fsolve(f, [5, math.radians(40)])      # podajemy funkcje, a potem initial guess
print("V: ", result[0])
print("Kat: ", math.degrees(result[1]))