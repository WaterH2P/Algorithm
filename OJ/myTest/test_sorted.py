N = [12, -32, 43, -49]
print( sorted(N, key=abs) )

S = ['bob', 'about', 'Zoo', 'Credit']
print( sorted(S, key=str.lower) )

# 闭包
def sum():
    def f(x):
        return lambda : x*x
    fs = []
    for i in range(3) :
        fs.append(f(i))
    return fs

f1, f2, f3 = sum()
print( f1() )
print( f2() )
print( f3() )