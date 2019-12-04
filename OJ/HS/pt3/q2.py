# class KDTreeNode:
#     def __init__(self, location, dimension=None, left=None, right=None):
#         self.location = location
#         self.dimension = dimension
#         self.left = left
#         self.right = right
#
#
# def gen_node(dimension, points):
#     if not points:
#         return None
#     points.sort(key=lambda x: x[dimension])
#     mid_pos = len(points) // 2
#     mid = points[mid_pos]
#     next_dimension = (dimension + 1) % 2
#     return KDTreeNode(
#         mid, dimension,
#         gen_node(next_dimension, points[:mid_pos]),
#         gen_node(next_dimension, points[mid_pos+1:])
#     )
#
#
# for t in range(int(input())):
#     origin = input().split(',')
#     points = [tuple(map(float, _.split())) for _ in origin]
#     x, y = map(float, input().split())
#     k = int(input())
#     route = []
#     root = gen_node(0, points)
#     print(root)
#     # node = find_node(root, x, y)
#     # res = []
#     # for p in route:
#     #     print(p.x, p.y)
#     #     res.append(origin[points.index((p.x, p.y))])
#     # # res.reverse()
#     # print(*(res[-k:]), sep=',')


# for t in range(int(input())):
#   origin = input().split(',')
#   points = [tuple(map(float, _.split())) for _ in origin]
#   x, y = map(float, input().split())
#   k = int(input())
#   distances = []
#   for idx, point in enumerate(points):
#     distance = ((point[0]-x)**2 + (point[1]-y)**2) ** 0.5
#     distances.append((idx, distance))
#   distances.sort(key=lambda p: p[1])
#   res = []
#   print(k)
#   for i in range(k):
#     res.append(origin[distances[i][0]])
#   print(distances)
#   print(*res, sep=',')

class KDTreeNode:
    def __init__(self, x, y, split=None):
        self.x = x
        self.y = y
        self.split = split
        self.left = None
        self.right = None
        self.reached = False


def gen_tree(points):
    if len(points) == 1:
        return KDTreeNode(points[0][0], points[0][1])
    # 方差
    sum_x = sum([x * x for (x, y) in points])
    sum_y = sum([y * y for (x, y) in points])
    if sum_x >= sum_y:
        xs = sorted([x for (x, y) in points])
        mid = xs[len(xs) // 2]
        left_points, right_points, node = [], [], None
        for (x, y) in points:
            if x > mid:
                right_points.append((x, y))
            elif x < mid:
                left_points.append((x, y))
            else:
                node = KDTreeNode(x, y, 'x')
        node.left = gen_tree(left_points)
        node.right = gen_tree(right_points)
        return node
    else:
        ys = sorted([y for (x, y) in points])
        mid = ys[len(ys) // 2]
        left_points, right_points, node = [], [], None
        for (x, y) in points:
            if y > mid:
                right_points.append((x, y))
            elif y < mid:
                left_points.append((x, y))
            else:
                node = KDTreeNode(x, y, 'y')
        node.left = gen_tree(left_points)
        node.right = gen_tree(right_points)
        return node


class Queue:
    def __init__(self, k=1):
        self.k = k
        self.queue = []
        self.base = (0, 0)

    def add(self, node: KDTreeNode):
        node.reached = True
        self.queue.append(node)
        self.queue.sort(key=lambda n: self.cal_dist(n))
        if len(self.queue) > self.k:
            self.queue.pop()
        return self.queue

    def cal_dist(self, node):
        return ((self.base[0]-x) ** 2 + (self.base[1]-y) ** 2) ** 0.5


queue = Queue()


def find_node(node, x, y):
    if node.left is None and node.right is None:
        queue.add(node)
        return
    elif node.split == 'x':
        if x > node.x:
            if node.right:
                find_node(node.right, x, y)
            else:
                queue.add(node)
        else:
            if node.left:
                find_node(node.left, x, y)
            else:
                queue.add(node)
    elif node.split == 'y':
        if y > node.y:
            return find_node(node.right, x, y) if node.right else node
        else:
            return find_node(node.left, x, y) if node.left else node
    else:
        return None


for t in range(int(input())):
    origin = input().split(',')
    points = [tuple(map(float, _.split())) for _ in origin]
    x, y = map(float, input().split())
    k = int(input())
    root = gen_tree(points)
    queue = Queue(k)
    queue.base = (x, y)
    node = find_node(root, x, y)
    res = []
    for p in queue.queue:
        res.append(origin[points.index((p.x, p.y))])
    # res.reverse()
    print(*(res[-k:]), sep=',')