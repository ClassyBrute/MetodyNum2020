import numpy as np

A = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
B = np.array([[4, 2, 0], [2, 5, 2], [0, 2, 4]])
w = np.array([[1], [-2], [3]])

AB = np.dot(A, B)
Aw = np.dot(A, w)
BAw = np.dot(B, np.dot(A, w))

print("Macierz AB: \n" + str(AB))
print("Macierz Aw: \n" + str(Aw))
print("Macierz BAw: \n" + str(BAw))
print("Wyznacznik macierzy A:")
print(np.around(np.linalg.det(A), 2))
print("Wyznacznik macierzy B:")
print(np.around(np.linalg.det(B), 2))

print("Macierz odwrotna do macierzy A: \n")
print(np.around(np.linalg.inv(A), 2))
print("Macierz odwrotna do macierzy B: \n")
print(np.around(np.linalg.inv(B), 2))
