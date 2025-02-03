# M 이상 N 이하의 소수를 모두 출력하는 프로그램
# M과 N은 1이상 1,000,000 이하
# 입력 예시
# M N

import sys
import math

M, N = map(int, sys.stdin.readline().split())    # map(변환함수, 변환객체), 변환함수: int, float 등 자료형

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False   # 0과 1은 소수가 아님.

for i in range(2, int(math.sqrt(N)) + 1):   # N의 제곱근까지만 확인
    if is_prime[i]:
        for j in range(i * i, N + 1, i):    # i(소수)의 배수 삭제
            is_prime[j] = False

for num in range(M, N + 1):
    if is_prime[num]:
        print(num)