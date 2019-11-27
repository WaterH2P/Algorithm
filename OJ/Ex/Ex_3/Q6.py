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
        points[0], points[index] = points[index], points[0]
        for x in range(n):
            edges[x][0], edges[x][index] = edges[x][index], edges[x][0]
        for y in range(n):
            edges[0][y], edges[index][y] = edges[index][y], edges[0][y]
    isNext = True
    pointLine = [0]
    preLine = [0]
    preLineT = []
    while isNext:
        isNext = False
        for x in preLine:
            for y in range(n):
                if y not in pointLine and edges[x][y] == 1:
                    preLineT.append(y)
                    pointLine.append(y)
                    isNext = True
        preLine = preLineT if len(preLineT) > 0 else []
        preLineT = []
    showStr = ''
    for i in pointLine:
        showStr += points[i] + ' '
    print(showStr.strip())Q