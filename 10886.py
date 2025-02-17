import sys

N = int(sys.stdin.readline())

vote = []

for _ in range(N):
    num = int(sys.stdin.readline())

    vote.append(num)

if vote.count(1) > vote.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')