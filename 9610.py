import sys

n = int(sys.stdin.readline())

coordinate = [0] * 5

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if x == 0 or y == 0:
        coordinate[0] += 1

    if x > 0 and y > 0:
        coordinate[1] += 1

    if x < 0 and y > 0:
        coordinate[2] += 1

    if x < 0 and y < 0:
        coordinate[3] += 1

    if x > 0 and y < 0:
        coordinate[4] += 1

for i in range(1, len(coordinate)):
    print(f'Q{i}: {coordinate[i]}')

print(f'AXIS: {coordinate[0]}')