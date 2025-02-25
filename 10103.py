import sys

n = int(sys.stdin.readline())

a, b = 100, 100

for _ in range(n):
    a1, b1 = map(int, sys.stdin.readline().split())

    if a1 == b1:
        continue

    if a1 > b1:
        b -= a1

    if a1 < b1:
        a -= b1

print(a)
print(b)