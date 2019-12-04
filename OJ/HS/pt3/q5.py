matrix = [[]]


def navi(pos, depth, reached):
    tmp = matrix[pos]
    new_reached = [*reached, pos]
    if len(matrix[0]) == len(new_reached):
        return depth + 1
    for idx, val in enumerate(tmp):
        if idx not in new_reached and val:
            return max(depth, navi(idx, depth + 1, new_reached))


for t in range(int(input())):
    n, start = input().split()
    n = int(n)
    nodes = input().split()
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for idx, j in enumerate((input().split())[1:]):
            matrix[i][idx] = int(j)
    start_pos = nodes.index(start)
    print(navi(start_pos, 0, []))
