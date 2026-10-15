n = int(input())

for d in [64, 32, 16, 8, 4, 2, 1]:
    k = n // d
    if k > 0:
        print(f"{k} ({d})")
    n = n % d