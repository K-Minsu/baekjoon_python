import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())

    GPA = 0.0
    lecture_point = 0

    for j in range(N):
        C, G = map(float, sys.stdin.readline().split())

        GPA += C * G

        lecture_point += int(C)

    print(lecture_point, round(GPA / lecture_point, 1))