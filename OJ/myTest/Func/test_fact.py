
# 递归
def fact(n):
    if n == 1 :
        return 1
    else :
        return n * fact(n-1)

# 尾递归
def fact2(n):
    return fact_iter(n, 1)

def fact_iter(n, res):
    if n == 1 :
        return res
    else :
        return fact_iter(n-1, n*res)

print( fact(2) )
print( fact(5) )

print( fact2(2) )
print( fact2(5) )