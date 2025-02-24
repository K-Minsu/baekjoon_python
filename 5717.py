import sys

while True:
    M, F = map(int, sys.stdin.readline().split())

    if M == F == 0:
        break

    print(M + F)