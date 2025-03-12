import sys

total = int(sys.stdin.readline())

for _ in range(9):
    n = int(sys.stdin.readline())

    total -= n

print(total)