import random

n = int(input("Anna pisteiden lukumäärä: "))
k = 0

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        k += 1

print(f"Pi:n arvo on noin {4 * k / n}")