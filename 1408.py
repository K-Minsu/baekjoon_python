import sys

h, m, s = map(int, sys.stdin.readline().split(':'))
end_h, end_m, end_s = map(int, sys.stdin.readline().split(':'))

ans_h, ans_m, ans_s = 0, 0, 0

if end_s < s:
    ans_s = (end_s + 60) - s

    end_m -= 1

else:
    ans_s = end_s - s

if end_m < m:
    ans_m = (end_m + 60) - m

    end_h -= 1

else:
    ans_m = end_m - m

if end_h < h:
    ans_h = (end_h + 24) - h

else:
    ans_h = end_h - h

print(f"{ans_h:02}:{ans_m:02}:{ans_s:02}")