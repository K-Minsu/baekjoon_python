import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    op = sys.stdin.readline().split()

    op[0] = float(op[0])

    for j in range(1, len(op)):
        if op[j] == '@':
            op[0] *= 3
        elif op[j] == '%':
            op[0] += 5
        elif op[j] == '#':
            op[0] -= 7

    print(f'{op[0]:.2f}')