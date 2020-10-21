import matplotlib.pyplot as plt

x0 = 0.1
lista = [x0]
n1 = range(0, 101)

for n in range(1, 101):
    x0 = 3.5 * x0 * (1 - x0)
    lista.append(x0)

plt.scatter(n1, lista)
plt.show()

print(lista)