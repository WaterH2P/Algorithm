maxLen = 0

def myDFS(edges, pointLine):
    n = len(edges)
    if len(pointLine) == 0:
        pointLine = [0]
    global maxLen
    maxLen = max(maxLen, len(pointLine))
    prePoint = pointLine[-1]
    for y in range(n):
        if y not in pointLine and edges[prePoint][y] == 1:
            myDFS(edges, [*pointLine, y])


for _ in range(int(input().strip())):
    n, start = input().strip().split()
    n = int(n)
    points = list(input().strip().split())
    edges = []
    for i in range(n):
        string = input().strip()
        pointKey = string.split()[0]
        edge = list(map(int, string[2:].split()))
        edges.append(edge)
    index = points.index(start)
    if index != 0 and index != -1:
        for x in range(n):
            edges[x][0], edges[x][index] = edges[x][index], edges[x][0]
        for y in range(n):
            edges[0][y], edges[index][y] = edges[index][y], edges[0][y]
    myDFS(edges, [])
    print(maxLen)
    maxLen = 0