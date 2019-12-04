from itertools import groupby, product
for u in range(int(input())):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]
    for i, j in product(range(1, n), range(m)):
        if matrix[i][j] and matrix[i-1][j]:
            matrix[i][j] += matrix[i-1][j]
    print(max([min(sub) * len(sub) for i in range(n) for sub in [list(v) for k, v in groupby(matrix[i], lambda x: not x) if not k]]))
