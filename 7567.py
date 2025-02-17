import sys

bowl = sys.stdin.readline().strip()

first_bowl = bowl[0]
height_bowl = 10

for i in range(1, len(bowl)):
    if first_bowl == bowl[i]:
        height_bowl += 5

    if first_bowl != bowl[i]:
        height_bowl += 10
        first_bowl = bowl[i]

print(height_bowl)