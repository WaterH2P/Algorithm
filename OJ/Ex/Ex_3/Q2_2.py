for _ in range(int(input().strip())):
    points = [list(map(int, item.split(' '))) for item in input().strip().split(',')]
    pointSearch = list(map(float, input().strip().split(' ')))
    k = int(input().strip())
    for point in points:
        dis = round((point[0] - pointSearch[0]) ** 2 + (point[1] - pointSearch[1]) ** 2, 3)
        point.append(dis)
    points.sort(key=lambda x: x[2])
    i = 0
    printStr = ''
    while i < k:
        printStr += str(points[i][0]) + ' ' + str(points[i][1]) + ','
        i += 1
    print(printStr[:-1])
