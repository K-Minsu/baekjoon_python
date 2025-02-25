import sys

A, B, C = 5 * 60, 1 * 60, 10
A_count, B_count, C_count = 0, 0, 0

T = int(sys.stdin.readline())

while True:
    if T - A < 0:
        break

    T -= A
    A_count += 1

while True:
    if T - B < 0:
        break

    T -= B
    B_count += 1

while True:
    if T - C < 0:
        break

    T -= C
    C_count += 1

if T > 0:
    print(-1)

else:
    print(A_count, B_count, C_count)