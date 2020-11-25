from scipy.optimize import newton
import numpy as np


def pierwiastek(a):
    f = lambda x, a: x**5 - a
    pochodna_f = lambda x, a: 5*x**4

    # zalozenie ile bedzie wynosic pierwiastek z liczby
    x = np.random.randn(2)

    print(newton(f, x, fprime = pochodna_f, args = (a, )))


# jako argument podajemy szukana podstawe pierwiastka
pierwiastek(243)