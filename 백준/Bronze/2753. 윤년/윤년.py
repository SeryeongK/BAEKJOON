import sys

input = int(sys.stdin.readline())

def year(y):
    # 윤년일 때
    if (y % 4 == 0 and y % 100 !=0) or y % 400 == 0:
        print(1)
    else:
        print(0)

year(input)