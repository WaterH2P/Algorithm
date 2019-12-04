from itertools import combinations
for t in range(int(input())):
    points = []
    for p in range(int(input())):
        x, y = map(int, input().split())
        points.append((x, y))
    from_x, from_y = dict(), dict()
    for (x, y) in points:
        if x in from_x:
            from_x[x].append(y)
        else:
            from_x[x] = [y]
        if y in from_y:
            from_y[y].append(x)
        else:
            from_y[y] = [x]
    count = 0
    for y_list in from_x.values():
        length = len(y_list)
        if length > 1:
            i = 0
            while i < length:
                j = i + 1
                while j < length:
                    if y_list[i] != y_list[j]:
                        count += 1
                    j += 1
                i += 1
    for x_list in from_y.values():
        length = len(x_list)
        if length > 1:
            i = 0
            while i < length:
                j = i + 1
                while j < length:
                    if x_list[i] != x_list[j]:
                        count += 1
                    j += 1
                i += 1
    print(count)
