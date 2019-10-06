
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print( L[0:2] )
print( L[:3] )
print( L[1:3] )
print( L[-2:] )
print( L[-2:-1] )

N = list(range(100))

# 前 10 个数，每两个取出
print( N[:10:2] )
# 所有数据，每五个取出
print( N[::5] )
# 复制 list
print( N[:] )

# tuple str 也可以做 slice
T = (1, 2, 3, 4, 5, 6)
S = 'abcdefghijklmn'

print( T[:3] )
print( S[2:7] )
