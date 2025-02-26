import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

number = []

for i in range(math.ceil(math.sqrt(M)), math.floor(math.sqrt(N)) + 1):
    number.append(i * i)

if len(number) == 0:
    print(-1)

else:
    print(sum(number))
    print(min(number))