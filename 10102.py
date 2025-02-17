import sys

V = int(sys.stdin.readline())
vote_list = sys.stdin.readline().strip()

if vote_list.count('A') > vote_list.count('B'):
    print('A')

if vote_list.count('A') == vote_list.count('B'):
    print('Tie')

if vote_list.count('A') < vote_list.count('B'):
    print('B')