import sys
i = 0
count = int( sys.stdin.readline().strip('\n') )
while i < count:
    a, b = map( int, sys.stdin.readline().strip('\n').split(' ') )
    print( a + b )
    i += 1