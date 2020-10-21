import numpy as np

print("Wyniki dla oryginalnego wyrażenia \n")
for n in range(2, 25, 2):
    x = pow(2, -n)
    wyr = np.sqrt(pow(x, 2) + 1) - 1
    print("n =", n, wyr)

# wyrażenie przekształcone tak aby nie zawierało odejmowania
print("Wyniki dla przekształconego wyrażenia \n")
for n in range(2, 25, 2):
    x = pow(2, -n)
    wyr = (pow(x, 2)) / (np.sqrt(pow(x, 2) + 1) + 1)
    print("n =", n, wyr)

print("Wyrażenie 2 wydaje się być dokładniejsze niż wyrazenie 1")
