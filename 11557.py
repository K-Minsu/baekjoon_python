import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    school_name = [0] * 3
    school_count = [0] * 3
    
    for i in range(N):
        name, count = map(str, sys.stdin.readline().split())

        count = int(count)

        school_name.append(name)
        school_count.append(count)

    idx = school_count.index(max(school_count))

    print(school_name[idx])