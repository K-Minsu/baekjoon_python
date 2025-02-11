import sys

score = 0

for i in range(0, 5):
    n = int(sys.stdin.readline())

    if n < 40:
        n = 40

    score += n

print(int(score / 5))