import sys

number1, number2 = map(int, sys.stdin.readline().split())

# 최대공약수 GCD
# 어떤 두 수의 최대공약수는 두 수 중 작은 수와 두 수의 나머지의 최대공약수와 같다.
# if a > b, GCD(a, b) = GCD(b, a % b)
# a % b가 0이 될 때까지 반복 -> 마지막에 나누는 수(a)가 두 수의 최대공약수가 된다.

def GCD(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

# 최소공배수 LCM
# 두 수의 곱은 GCD와 LCM의 곱과 같다.
# a * b = GCD(a, b) * LCM(a, b)
# 즉, LCM(a, b) = (a * b) / GCD(a, b)

gcd = GCD(number1, number2)
lcm = (number1 * number2) / gcd

print(gcd)
print(int(lcm))