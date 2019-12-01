def twoPointsNeighbor(x1, y1, xDraw, yDraw, xGive, yGive):
    return ((xGive == x1 and yGive == y1) or (xGive == x1 + 1 and yGive == y1) or (xGive == x1 and yGive == y1 + 1) or (xGive == x1 + 1 and yGive == y1 + 1)) \
           and \
           not ((xGive <= x1 and yGive <= y1 and xDraw <= x1 and yDraw <= y1) or (xGive <= x1 and yGive > y1 and xDraw <= x1 and yDraw > y1)
                or
                (xGive > x1 and yGive <= y1 and xDraw > x1 and yDraw <= y1) or (xGive > x1 and yGive > y1 and xDraw > x1 and yDraw > y1))


def findNeighbor(n, xDraw, yDraw, xGive, yGive, xStart, yStart):
    xymid = 2 ** (n - 1) - 1
    # print(xymid, xymid, ',', xDraw, yDraw, ',', xGive, yGive, ',', xStart, yStart)
    if n == 1 or twoPointsNeighbor(xymid, xymid, xDraw, yDraw, xGive, yGive):
        # print('1 -->')
        if n != 1:
            xDraw = xymid if xDraw <= xymid else xymid + 1
            yDraw = xymid if yDraw <= xymid else xymid + 1
        points = [[xymid, xymid], [xymid + 1, xymid], [xymid, xymid + 1], [xymid + 1, xymid + 1]]
        for i in range(len(points)):
            point = points[i]
            if point[0] == xDraw and point[1] == yDraw:
                points.pop(i)
                break
        for i in range(len(points)):
            point = points[i]
            if point[0] == xGive and point[1] == yGive:
                points.pop(i)
                break
        for i in range(len(points)):
            points[i][0] += xStart
            points[i][1] += yStart
        points.sort(key=lambda x: (x[0], x[1]))
        return points
    else:
        # print('2 -->')
        lost = xymid + 1
        if xGive <= xymid:
            if yGive <= xymid:
                if xDraw <= xymid and yDraw <= xymid:
                    return findNeighbor(n - 1, xDraw, yDraw, xGive, yGive, xStart, yStart)
                else:
                    return findNeighbor(n - 1, xymid, xymid, xGive, yGive, xStart, yStart)
            else:
                if xDraw <= xymid and yDraw > xymid:
                    return findNeighbor(n - 1, xDraw, yDraw - lost, xGive, yGive - lost, xStart, yStart + lost)
                else:
                    return findNeighbor(n - 1, xymid, 0, xGive, yGive - lost, xStart, yStart + lost)
        else:
            if yGive <= xymid:
                if xDraw > xymid and yDraw <= xymid:
                    return findNeighbor(n - 1, xDraw - lost, yDraw, xGive - lost, yGive, xStart + lost, yStart)
                else:
                    return findNeighbor(n - 1, 0, xymid, xGive - lost, yGive, xStart + lost, yStart)
            else:
                if xDraw > xymid and yDraw > xymid:
                    return findNeighbor(n - 1, xDraw - lost, yDraw - lost, xGive - lost, yGive - lost, xStart + lost,
                                        yStart + lost)
                else:
                    return findNeighbor(n - 1, 0, 0, xGive - lost, yGive - lost, xStart + lost, yStart + lost)


for _ in range(int(input().strip())):
    n, xDraw, yDraw = map(int, input().strip().split())
    xGive, yGive = map(int, input().strip().split())
    xStart, yStart = 0, 0
    neighbors = findNeighbor(n, xDraw, yDraw, xGive, yGive, 0, 0)
    printStr = ''
    for neighbor in neighbors:
        printStr += str(neighbor[0]) + ' ' + str(neighbor[1]) + ','
    print(printStr[:-1])
