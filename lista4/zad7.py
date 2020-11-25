from sympy import Symbol, solve

x = Symbol('x')

eq1 = x**4 + (5 + 1j) * x**3 - (8 - 5j) * x**2 + (30 - 14j) * x - 84

result = solve(eq1, x)

print("Miejsca zerowe funkcji: ")
print(result)