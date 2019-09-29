def power(x, n=2):
    if n < 0:
        return 0
    else:
        sum = 1
        while n > 0:
            sum *= x
            n -= 1
        return sum

val = power(2, 4)
print(val)