def hlt(n, t1, t2, t3, sumOp):
    if n == 1 :
        if t1 == 'a' and t3 == 'c' :
            sumOp += 2
        elif t1 == 'c' and t3 == 'a' :
            sumOp += 2
        else :
            sumOp += 1
        return sumOp
    else :
        sumOp = hlt(n-1, t1, t2, t3, sumOp)
        sumOp = hlt(1, t1, t3, t2, sumOp)
        sumOp = hlt(n-1, t3, t2, t1, sumOp)
        sumOp = hlt(1, t2, t1, t3, sumOp)
        sumOp = hlt(n-1, t1, t2, t3, sumOp)
        return sumOp

n = int(input().strip())
for k in range(n) :
    sumOp = 0
    N = int(input().strip())
    if N == 1 :
        print(2)
    else :
        sumOp = hlt(N, 'a', 'b', 'c', 0)
        print(sumOp)