import sys

n = int(sys.stdin.readline())

data_list = [] * n

for _ in range(n):
    name, day, month, year = map(str, sys.stdin.readline().strip().split())
    
    data_list.append([int(year), int(month), int(day), name])

data_list.sort(key=lambda x:(x[0], x[1], x[2]))

print(data_list[n - 1][3])
print(data_list[0][3])