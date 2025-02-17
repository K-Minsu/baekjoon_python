import sys

N = int(sys.stdin.readline())

people = []

for _ in range(N):
    n1, n2, n3 = map(int, sys.stdin.readline().split())

    award = 0

    if n1 == n2 == n3:
        award = 10000 + n1 * 1000

    if n1 == n2 and n1 != n3:
        award = 1000 + n1 * 100

    if n2 == n3 and n2 != n1:
        award = 1000 + n2 * 100

    if n3 == n1 and n3 != n2:
        award = 1000 + n3 * 100

    if n1 != n2 and n2 != n3 and n3 != n1:
        award = max(n1, n2, n3) * 100

    people.append(award)

print(max(people))