import sys
str = sys.stdin.readline().strip('\n')
while ( len(str) > 0 ):
    a, b = map( int, str.split(' ') )
    print( a + b )
    str = sys.stdin.readline().strip('\n')
