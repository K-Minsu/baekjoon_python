# 유클리드 호제법
# 먼저 최대공약수를 구한다
# 어떤 두 수의 최대공약수는 두 수 중 작은 수와 두 수의 나머지의 최대공약수와 같다.
# if a > b, GCD(a, b) = GCD(b, a mod b)
# a mod b가 0이 될 때까지 반복 -> 마지막에 나누는 수가 두 수의 최대공약수가 된다.

# 그럼 최소공배수는 어떻게 구하는가?
# GCD와 LCM의 관계
# 두 수의 곱은 GCD와 LCM의 곱과 같다. (a * b) / GCD(a, b) = LCM(a, b)

import sys

def GCD(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b

    return a

T = int(sys.stdin.readline())

while(T):
    A, B = map(int, sys.stdin.readline().split())

    print(abs(A * B) // GCD(A, B))

    T -= 1