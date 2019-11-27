
# 匈牙利算法
# https://www.cnblogs.com/rainsoul/p/8467160.html

jobGives = []

# 找到最少的水平线或垂直线覆盖矩阵所有的 0
def matrixCover(matrix):
    n = len(matrix)
    isRow, isCol = False, False
    # 行或者列 0 最多的 index
    rowI, colI = -1, -1
    # 行或者列 0 最多的个数
    zeroCountMax = 0
    lineCover = 0
    # 保存已被覆盖的行或者列
    matrixT = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            matrixT[x][y] = matrix[x][y]
    isCover = False
    removeNum = -999
    # coverInfo[0] : True or False 表示最少覆盖是否等于矩阵大小
    # coverInfo[1] : 覆盖行的 index
    # coverInfo[2] : 覆盖列的 index
    # coverInfo[3] : 未覆盖的最小值
    coverInfo = [False, [], [], []]
    while not isCover:
        isCover = True
        for x in range(n):
            if x not in coverInfo[1]:
                zeroCount = matrix[x].count(0)
                zeroCount1 = matrixT[x].count(0)
                if zeroCount > zeroCountMax and zeroCount1 > 0:
                    zeroCountMax = zeroCount
                    rowI, isRow = x, True
                    colI, isCol = -1, False
        for y in range(n):
            if y not in coverInfo[2]:
                zeroCount = [item[y] for item in matrix].count(0)
                zeroCount1 = [item[y] for item in matrixT].count(0)
                if zeroCount > zeroCountMax and zeroCount1 > 0:
                    zeroCountMax = zeroCount
                    rowI, isRow = -1, False
                    colI, isCol = y, True
        if (isRow and rowI > -1) or (isCol and colI > -1):
            if isRow:
                coverInfo[1].append(rowI)
                for y in range(n):
                    matrixT[rowI][y] = removeNum
            elif isCol:
                coverInfo[2].append(colI)
                for x in range(n):
                    matrixT[x][colI] = removeNum
            lineCover += 1

            if lineCover < n:
                zeroCountMax = 0
                isRow, isCol = False, False
                rowI, colI = -1, -1
                isCover = False
            else:
                coverInfo[0] = True
                return coverInfo
        else:
            # 未能实现最少的水平线或垂直线覆盖矩阵所有的 0 的数量为矩阵大小
            if lineCover < n:
                coverInfo[0] = False
                # 未被覆盖区域的最小值
                minNum = 9999
                for x in range(n):
                    if x not in coverInfo[1]:
                        for y in range(n):
                            if y not in coverInfo[2]:
                                if 0 < matrixT[x][y] < minNum:
                                    minNum = matrixT[x][y]
                coverInfo[3] = minNum
                return coverInfo

# 将矩阵转化为 最少的水平线或垂直线覆盖所有的 0 的个数为矩阵大小
def matrixTransform(matrixT):
    n = len(matrixT)
    matrix = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            matrix[x][y] = matrixT[x][y]
    for x in range(n):
        minNum = min(*matrix[x])
        for y in range(n):
            matrix[x][y] -= minNum
    for y in range(n):
        minNum = min(*[item[y] for item in matrix])
        for x in range(n):
            matrix[x][y] -= minNum
    coverInfo = matrixCover(matrix)
    while not coverInfo[0]:
        # 没有被覆盖的每行减去最小值，被覆盖的每列加上最小值
        for x in range(n):
            if x not in coverInfo[1]:
                for y in range(n):
                    matrix[x][y] -= coverInfo[3]
        for y in coverInfo[2]:
            for x in range(n):
                matrix[x][y] += coverInfo[3]
        coverInfo = matrixCover(matrix)
    return matrix

# 任务分配，递归暴力破解
def matrixJobGive(matrix, jobGive, minIndex):
    n = len(matrix)
    for x in range(n):
        if jobGive[x] == -1:
            for y in range(n):
                if y > minIndex and matrix[x][y] == 0 and y not in jobGive:
                    jobGive[x] = y
                    minIndex = -1
                    break
    if -1 not in jobGive:
        jobGives.append([_ for _ in jobGive])
        minIndex = jobGive[-1]
        jobGive[-1] = -1
        matrixJobGive(matrix, jobGive, minIndex)
        return None
    else:
        index = jobGive.index(-1)
        if index == 0:
            return None
        else:
            minIndex = jobGive[index-1]
            for x in range(index-1, n):
                jobGive[x] = -1
            matrixJobGive(matrix, jobGive, minIndex)
            return None


for _ in range(int(input().strip())):
    jobNum = int(input().strip())
    costsArray = [map(int, item.split(' ')) for item in input().strip().split(',')]
    costs = [[0]*jobNum for _ in range(jobNum)]
    for x, y, c in costsArray:
        costs[x-1][y-1] = c
    costs = matrixTransform(costs)
    matrixJobGive(costs, [-1]*jobNum, -1)
    jobGives.sort(reverse=True)
    jobGivesStr = []
    for item in jobGives:
        jobGivesStr.append(' '.join([str(_+1) for _ in item]))
    jobGives = []
    print(*jobGivesStr, sep=',')
