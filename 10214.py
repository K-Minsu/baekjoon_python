import sys

T = int(sys.stdin.readline())

for _ in range(T):
    Yonsei, Korea = 0, 0
    
    for __ in range(9):
        Y, K = map(int, sys.stdin.readline().split())

        Yonsei += Y
        Korea += K

    if Yonsei == Korea:
        print('Draw')

    if Yonsei > Korea:
        print('Yonsei')

    if Yonsei < Korea:
        print('Korea')