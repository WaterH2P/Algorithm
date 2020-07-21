class Solution:
    def frogPosition(self, n: int, edges, t: int, target: int) -> float:
        if target == 1:
            return 1 if len(edges) == 0 else 0
        res, road, isTargetEnd = 1.0, [target], True
        for i in range(0, len(edges)):
            if edges[i][0] > edges[i][1]:
                edges[i][0], edges[i][1] = edges[i][1], edges[i][0]
            if edges[i][0] == target:
                isTargetEnd = False
        while road[0] != 1:
            for edge in edges:
                if road[0] == edge[1]:
                    road.insert(0, edge[0])
                    break
        road.pop(-1)
        if ( t > len(road) and not isTargetEnd ) or t < len(road):
            return 0
        while len(road) > 0:
            step, count, i = road.pop(0), 0.0, 0
            while i < len(edges):
                if step == edges[i][0]:
                    edges.pop(i)
                    count += 1.0
                else:
                    i += 1
            if count > 0:
                res /= count
        return res

# n = 7
# edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
# t = 2
# target = 4

# result = 0.3333333333333333
# n = 7
# edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
# t = 1
# target = 7

# result = 0.16666666666666666
# n = 7
# edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
# t = 20
# target = 6

# result = 1
# n = 3
# edges = [[2,1],[3,2]]
# t = 1
# target = 2

result = 0
n = 8
edges = [[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]]
t = 7
target = 7

# result = 0
# n = 9
# edges = [[2,1],[3,1],[4,2],[5,3],[6,5],[7,4],[8,7],[9,7]]
# t = 1
# target = 8

s = Solution()
print( s.frogPosition(n, edges, t, target) )
        