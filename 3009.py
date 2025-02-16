import sys

forth_coordinate_x = []
forth_coordinate_y = []

check_coordinate_x = 0
check_coordinate_y = 0

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())

    if x in forth_coordinate_x:
        check_coordinate_x = x

    if y in forth_coordinate_y:
        check_coordinate_y = y

    if x not in forth_coordinate_x:
        forth_coordinate_x.append(x)
    
    if y not in forth_coordinate_y:
        forth_coordinate_y.append(y)

for coor in forth_coordinate_x:
    if coor != check_coordinate_x:
        print(coor, end=' ')

for coor in forth_coordinate_y:
    if coor != check_coordinate_y:
        print(coor)