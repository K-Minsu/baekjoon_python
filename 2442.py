import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    for j in range(i, N):
        print(' ', end='')

    for k in range(1, 2 * i):
        print('*', end='')

    print()