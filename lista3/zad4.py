import copy

def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1

    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i] / a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t * a[i][k]
            for k in range(p):
                b[j][k] -= t * b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t * b[j][k]
        t = 1 / a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t

    return b

# macierze z zadania 1
A = [[-1, 1, -4],
     [2, 2, 0],
     [3, 3, 2]]

B = [[0],
     [1],
     [0.5]]

zad1 = gauss(A, B)

print("Rozwiazanie zadania 1 = " + str(zad1))


# macierze z zadania 2
L = [[1, 0, 0],
     [3/2, 1, 0],
     [1/2, 11/13, 1]]

U = [[2, -3, -1],
     [0, 13/2, -7/2],
     [0, 0, 32/13]]

B = [[1],
     [-1],
     [2]]

y = gauss(L, B)
zad2 = gauss(U, y)

print("Rozwiazanie zadania 2 = " + str(zad2))


# macierze z zadania 3
A = [[0, 0, 2, 1, 2],
     [0, 1, 0, 2, -1],
     [1, 2, 0, -2, 0],
     [0, 0, 0, -1, 1],
     [0, 1, -1, 1, -1]]

B = [[1],
     [1],
     [-4],
     [-2],
     [-1]]

zad3 = gauss(A, B)

print("Rozwiazanie zadania 3 = " + str(zad3))