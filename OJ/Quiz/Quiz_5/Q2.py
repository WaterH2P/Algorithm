for _ in range(int(input().strip())):
    n = int(input().strip())
    times = [[0, 0] for i in range(n)]
    arrives = list(map(int, input().strip().split()))
    leaves = list(map(int, input().strip().split()))
    for i in range(n):
        times[i][0] = arrives[i]
        times[i][1] = leaves[i]
    stations = []
    for train in times:
        if len(stations) == 0:
            stations.append(train[1])
        else:
            isIn = False
            for i in range(len(stations)):
                if train[0] > stations[i]:
                    stations[i] = train[1]
                    isIn = True
                    break
            if not isIn:
                stations.append(train[1])
    print(len(stations))