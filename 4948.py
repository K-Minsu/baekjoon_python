import sys
import math

def is_prime(n1, n2):
    prime = [True] * (n2 + 1)
    prime[0] = prime[1] = False
    cnt = 0

    for i in range(2, int(math.sqrt(n2)) + 1):
        if prime[i] == True:
            for j in range(i * i, n2 + 1, i):
                prime[j] = False

    for num in range(n1 + 1, n2 + 1):
        if prime[num] == True:
            cnt += 1

    return cnt


while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    ans = is_prime(n, 2 * n)

    print(ans)