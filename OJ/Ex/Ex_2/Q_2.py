def calMaxMatrix(matrix, l, r, u, d):
    if r <= l or d <= u :
        return -1
    maxCount = -1
    j = -1
    row = u-1
    col = l
    while row < d-1 and j < 0 :
        row += 1
        col = l
        while col < r :
            if matrix[row][col] == 0 :
                j = col
                break
            col += 1
    if j > -1 :
        lMax = calMaxMatrix(matrix, l, j, u, d)
        rMax = calMaxMatrix(matrix, j+1, r, u, d)
        uMax = calMaxMatrix(matrix, l, r, u, row)
        dMax = calMaxMatrix(matrix, l, r, row+1, d)
        maxCount = max(lMax, rMax, uMax, dMax)
    if maxCount < 0 :
        maxCount = (r-l)*(d-u)
    return maxCount

n = int(input().strip())
for k in range(n) :
    row, col = map(int, input().strip().split())
    matrix = []
    for j in range(row) :
        nums = list( map(int, input().strip().split()) )
        while len(nums) < col :
            nums.append(0)
        if len(nums) > col :
            nums = nums[:col]
        matrix.append(nums)
    maxCount = calMaxMatrix(matrix, 0, col, 0, row)
    print(maxCount)

