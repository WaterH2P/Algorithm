# Given arrival and departure times of all trains that reach a railway station. 
# Your task is to find the minimum number of platforms required for the railway station so that no train waits. 
# Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times must not be same for a train.

for _ in range(int(input().strip())):
    n = int(input().strip())
    inTs = list(map(int, input().strip().split()))
    goTs = list(map(int, input().strip().split()))
    stations = []
    for i in range(n):
        inT, goT = inTs[i], goTs[i]
        isIn = False
        for station in stations:
            if inT > station[0]:
                station[0] = goT
                isIn = True
                break
        if not isIn:
            stations.append([goT])
    print(len(stations))