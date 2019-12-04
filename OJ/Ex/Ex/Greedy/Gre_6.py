# Given a square grid of size n, each cell of which contains integer cost which represents a cost to traverse through that cell, 
# we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum.
# Note : It is assumed that negative cost cycles do not exist in input matrix.

for _ in range(int(input().strip())):
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    matrix = [[0]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            matrix[x][y] = nums[x*n+y]
    # for item in matrix:
    #     print(item)
    # print('')
    costs = [[999]*n for i in range(n)]
    for y in range(n):
        costs[0][y] = sum(matrix[0][0:y+1])
    for x in range(n):
        cost = 0
        for j in range(x+1):
            cost += matrix[j][0]
        costs[x][0] = cost
    x = 0
    while x < n:
        y = 0
        isExist = False
        while y < n:
            if x < n - 1:
                costs[x][y] = min(costs[x][y], costs[x+1][y] + matrix[x][y])
            if y < n - 1:
                costs[x][y] = min(costs[x][y], costs[x][y+1] + matrix[x][y])
            if x > 0:
                costs[x][y] = min(costs[x][y], costs[x-1][y] + matrix[x][y])
            if y > 0:
                costs[x][y] = min(costs[x][y], costs[x][y-1] + matrix[x][y])
            
            # 存在往左走的可能
            if x > 0 and costs[x][y] + matrix[x-1][y] < costs[x-1][y]:
                isExist = True
            # 存在往上走的可能
            if y > 0 and costs[x][y] + matrix[x][y-1] < costs[x][y-1]:
                isExist = True
            y += 1
        if isExist:
            x -= 1
        else:
            x += 1
    # for item in costs:
    #     print(item)
    print(costs[-1][-1])