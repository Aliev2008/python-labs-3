s = 0
count = 0

x = int(input())
while x != 0:
    s += x
    count += 1
    x = int(input())

print(s / count)