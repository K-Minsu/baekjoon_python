import sys

K, N, M = map(int, sys.stdin.readline().split())

if K * N > M:
    print(int(K * N) - M)
else:
    print(0)