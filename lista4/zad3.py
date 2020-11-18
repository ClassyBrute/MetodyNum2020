import numpy as np

for t in range(0, 1000):
    u = 2510
    M = 2.8 * 10**6
    m = 13.3 * 10**3
    g = 9.81

    v = u * np.log(M / (M - m * t)) - (g * t)

    if v >= 335:
        print("Osiagnie 335km/h po " + str(t) + " sekundach")
        break
