for t in range(int(input())):
  origin = input().strip().split(',')
  points = [tuple(map(float, point.split())) for point in origin]
  x, y = map(float, input().split())
  k = int(input())
  distances = []
  for idx, point in enumerate(points):
    distance = ((point[0]-x)**2 + (point[1]-y)**2) ** 0.5
    tx, ty = point[0], point[1]
    xs, ys = str(tx), str(ty)
    if int(tx) == float(tx):
      xs = str(int(tx))
    if int(ty) == float(ty):
      ys = str(int(ty))
    distances.append((distance, xs+' '+ys))
  # print(distances)
  distances.sort(key=lambda p: p[0])
  print(*([_[1] for _ in distances][:k]), sep=',')

