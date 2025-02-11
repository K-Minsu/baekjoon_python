import sys

S = int(sys.stdin.readline())

cnt, idx = 0, 0

while(True):
    cnt += idx

    if cnt > S:
        break

    idx += 1

print(idx - 1)