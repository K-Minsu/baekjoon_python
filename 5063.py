import sys

N = int(sys.stdin.readline())

for _ in range(N):
    r, e, c = map(int, sys.stdin.readline().split())

    if e - c > r:
        print('advertise')

    if e - c == r:
        print('does not matter')

    if e - c < r:
        print('do not advertise')