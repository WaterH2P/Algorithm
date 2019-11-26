for _ in range(int(input().strip())):
    N, X, Y = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    diff = []
    for i in range(len(A)):
        if A[i] > B[i]:
            diff.append(A[i]-B[i])
        else:
            diff.append(B[i] - A[i])
    maxSum = 0
    maxNum = -1
    while X > 0 and Y > 0:
        maxNum = max(*diff)
        index = diff.index(maxNum)
        if A[index] > B[index]:
            maxSum += A[index]
            X -= 1
        else:
            maxSum += B[index]
            Y -= 1
        A.pop(index)
        B.pop(index)
    if X > 0:
        maxSum += sum(A)
    elif Y > 0:
        maxSum += sum(B)
    print(maxSum)