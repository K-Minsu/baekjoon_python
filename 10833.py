import sys

N = int(sys.stdin.readline())

remain_apple = 0

for i in range(N):
    student, apple = map(int, sys.stdin.readline().split())

    remain_apple += apple % student

print(remain_apple)