import numpy as np

print("Wyniki dla oryginalnego wyrażenia \n")
for n in range(2, 21, 2):
    x = pow(2, -n)
    wyr = np.sqrt(pow(x, 4) + 4) - 2
    print("n =", n, wyr)

# wyrażenie przekształcone tak aby nie zawierało odejmowania
print("Wyniki dla przekształconego wyrażenia \n")
for n in range(2, 21, 2):
    x = pow(2, -n)
    wyr = pow(x, 4) / (np.sqrt(pow(x, 4) + 4) + 2)
    print("n =", n, wyr)

print("Wyrażenie 1 przestaje być dokładne przy n=14, a "
      "wyrażenie 2 nawet przy n=20 wciąż daje dobre wyniki")