import numpy as np

# nie n-1, bo range nie uwzględnia ostatniej liczby
def macierz(u, arr, p = 0):
    for i in range(p, u):
        for k in range(p, u):
            h = 1 / (i + k + 1)
            arr[i][k] = h
    return arr

n = 4   # n dla macierzy 4x4
n1 = 8  # n dla macierzy 8x8
A = [[0]*n for s in range(n)] # tworzy pustą macierz 4x4
B = [[0]*n1 for s1 in range(n1)] # tworzy pustą macierz 8x8

macierz(n, A)   # macierz 4x4
macierz(n1, B)  # macierz 8x8

# wyznacznik dla n od 5 do 21
for g in range(5, 20):
    C = [[0] * g for s2 in range(g)]

    macierz(g, C)

    print("Wyznacznik macierzy " + str(g) + "x" + str(g) + ": ")
    print('{:.2e}'.format(np.linalg.det(C)))


# wyświetla macierz 4x4 łatwą do odczytania
# np.around zaokrągla do 2 miejsc po przecinku
print("Macierz Hilberta 4x4")
for n in A:
    print(np.around(n, 2))

print('\n')

print("Macierz odwrotna Hilberta 4x4")
print(np.around(np.linalg.inv(A), 2))

print('\n')

print("Macierz Hilberta 8x8")
for n1 in B:
    print(np.around(n1, 3))

# jak zaokrąglić wszystkie liczby w macierzy?
print("Macierz odwrotna Hilberta 8x8")
print(np.linalg.inv(B))