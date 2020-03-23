# 【中等】841. 钥匙和房间
# 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
# 在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，
# 其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。
# 最初，除 0 号房间外的其余所有房间都被锁住。
# 你可以自由地在房间之间来回走动。
# 如果能进入每个房间返回 true，否则返回 false。


# dfs
class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        keys = set()
        def findKey(key):
            keys.add(key)
            [findKey(keyT) for keyT in rooms[key] if keyT not in keys]
        return findKey(0) or len(keys) == len(rooms)


# bfs
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit, keys = [False] * len(rooms), [0]
        while len(keys) > 0:
            key = keys.pop()
            visit[key] = True
            for i in rooms[key]:
                if not visit[i]: keys.append(i)
        return len(list(filter(lambda x: not x, visit))) == 0


if __name__ == '__main__':
    s = Solution()

    result = True
    rooms = [[1],[2],[3],[]]
    print(s.canVisitAllRooms(rooms))

    result = False
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(s.canVisitAllRooms(rooms))