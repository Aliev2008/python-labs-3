import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        n = int(line)
        print(*range(10 + n, 100, 10))