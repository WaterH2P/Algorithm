def divBoard(numP, boardT, minT):
    if numP > len(boardT) or numP < 0 or len(boardT) == 0:
        return 99999
    elif numP == 1 :
        return sum(boardT)
    elif numP == len(boardT) :
        return max(boardT)
    
    sum1, sum2 = 0, sum(boardT)
    for i in range(0, len(boardT)-(numP-1)) :
        sum1 += boardT[i]
        sum2 -= boardT[i]
        minT = min(minT, max(sum1, sum2))
        if sum1 >= minT or sum1 >= sum2:
            break
        minSum2 = divBoard(numP-1, boardT[i+1:], minT)
        minT = min(minT, minSum2)
    return minT

n = int(input().strip())
for k in range(n) :
    numP, numB = map(int, input().strip().split())
    boardT = list(map(int, input().strip().split()))
    boardT = boardT[:numB]
    minT = divBoard(numP, boardT, sum(boardT))
    print(minT)