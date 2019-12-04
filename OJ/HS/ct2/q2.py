class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def left_most(points):
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convex_hull(points, n):
    if n < 3:
        print(-1)
        return
    l = left_most(points)
    hull = []
    p = l
    q = 0
    while True:
        hull.append(p)
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    res = sorted([(points[each].x, points[each].y) for each in hull], key=lambda a: a[0])
    print(', '.join(map(lambda a: str(a[0]) + ' ' + str(a[1]), res)))


for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    convex_hull([Point(arr[2*i], arr[2*i+1]) for i in range(n)], n)



