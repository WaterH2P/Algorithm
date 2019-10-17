
def BB(pointA, pointB, points):
    pass

n = int(input().strip())
points = []
for k in range(n) :
    numP = int(input().strip())
    zb = list(map(int, input().strip().split()))
    i = 0
    while i < len(zb)-1 :
        points.append((zb[i], zb[i+1]))
        i += 2
    points.sort(key=lambda x: (x[0], x[1]))