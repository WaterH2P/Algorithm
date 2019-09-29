
# 生成器
# 用 () 代替 []
G = ( x*x for x in range(1, 11) )
for g in G :
    print(g)

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max :
        print(b)
        a, b = b, a+b
        n += 1

print('')
fib(8)

# 斐波拉契数列 generator
def fibG(max):
    n, a, b = 0, 0, 1
    while n < max :
        yield b
        a, b = b, a+b
        n += 1
    return 'done'

F = fibG(6)
print( [f for f in F] )

# 捕获 generator return 值
F2 = fibG(6)
while True :
    try:
        f = next(F2)
        print(f)
    except StopIteration as e:
        print( 'Generator return value:', e.value )
        break