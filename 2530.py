import sys

A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())

sec = A * 3600 + B * 60 + C + D

A = sec // 3600
B = (sec % 3600) // 60
C = (sec % 3600) % 60

print(A % 24, B, C)