import numpy as np
import scipy.integrate as integ

# podana funkcja
def f(theta, theta0):
    result = 1 / np.sqrt(1 - np.sin(theta0 / 2)**2 * np.sin(theta)**2)
    return result

h1 = np.pi/12 # podany kąt
result_h1 = integ.quad(f, 0, np.pi/2, args=h1) # wynik
print("h(15 stopni)")
print(f"Kąt = {h1*180/np.pi}, Wynik = {result_h1[0]}, Różnica między h(0) = {np.pi/2 - result_h1[0]}\n")

h2 = np.pi/6
result_h2 = integ.quad(f, 0, np.pi/2, args=h2)
print("h(30 stopni)")
print(f"Kąt = {h2*180/np.pi}, Wynik = {result_h2[0]}, Różnica między h(0) = {np.pi/2 - result_h2[0]}\n")

h3 = np.pi/4
result_h3 = integ.quad(f, 0, np.pi/2, args=h3)
print("h(45 stopni)")
print(f"Kąt = {h3*180/np.pi}, Wynik = {result_h3[0]}, Różnica między h(0) = {np.pi/2 - result_h3[0]}\n")
