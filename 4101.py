import sys

while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == b == 0:
        break
    elif a > b: print("Yes")
    elif a < b or a == b: print("No")