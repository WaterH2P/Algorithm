import sys
str = sys.stdin.readline().split()
while str:
    print(int(str[0]) + int(str[1]))
    print('')
    str = sys.stdin.readline().split()