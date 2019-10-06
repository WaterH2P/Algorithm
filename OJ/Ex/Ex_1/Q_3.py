import sys
str = sys.stdin.readline().strip('\n')
while ( len(str) > 0 ):
    a, b = map( int, str.split(' ') )
    if a == 0:
        if b == 0:
            break
    print( a + b )
    str = sys.stdin.readline().strip('\n')