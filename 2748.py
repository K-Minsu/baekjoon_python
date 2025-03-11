import sys

n = int(sys.stdin.readline())

def Fibo(n):
    f = [0] * (n + 1)
    
    f[0], f[1] = 0, 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]

print(Fibo(n))