import sys

n = int(sys.stdin.readline())

for i in range(n):
    p = int(sys.stdin.readline())

    cost = [] * p
    p_name = [] * p

    for j in range(p):
        C, name = map(str, sys.stdin.readline().strip().split())

        cost.append(int(C))
        p_name.append(name)

    print(p_name[cost.index(max(cost))])