import sys

N = int(sys.stdin.readline())

for i in range(N):
    for _ in range(0, i):
        print(' ', end='')

    for _ in range(N - i, 0, -1):
        print('*', end='')

    print()