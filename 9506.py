import sys

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break

    divisor = []

    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)

    if sum(divisor) == n:
        print(f'{n} =', end='')
        
        idx = 0
        while True:
            print(f' {divisor[idx]}', end='')

            if idx == len(divisor) - 1:
                print()
                break

            print(' +', end='')
            idx += 1

    else:
        print(f'{n} is NOT perfect.')