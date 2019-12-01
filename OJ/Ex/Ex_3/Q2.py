import math

def mkKDTree(points, node):
    print(points)
    print(node)
    print('')
    if len(points) == 1:
        node[0] = [points[0][0], points[0][1]]
    elif len(points) > 1:
        xAve, yAve = 0, 0
        for point in points:
            xAve += point[0]
            yAve += point[1]
        xAve /= len(points)
        yAve /= len(points)
        xVar, yVar = 0, 0
        for point in points:
            xVar += (point[0] - xAve) ** 2
            yVar += (point[1] - yAve) ** 2
        if xVar > yVar:
            points.sort(key=lambda x: x[0])
        else:
            points.sort(key=lambda x: x[1])
        midI = math.floor(len(points) / 2)
        node[0] = [points[midI][0], points[midI][1]]
        node[1] = [[0, 0], [], []]
        node[2] = [[0, 0], [], []]
        mkKDTree(points[:midI], node[1])
        mkKDTree(points[midI + 1:], node[2])


for _ in range(int(input().strip())):
    points = [list(map(int, item.split(' '))) for item in input().strip().split(',')]
    pointSearch = input().strip().split(' ')
    k = int(input().strip())
    kdTree = [[0, 0], [], []]
    mkKDTree(points, kdTree)
    print(kdTree)
