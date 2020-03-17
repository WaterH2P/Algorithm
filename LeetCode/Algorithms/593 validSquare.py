# 【中等】593. 有效的正方形
# 给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。
# 一个点的坐标（x，y）由一个有两个整数的整数数组表示。


class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        def dis2(p1, p2): return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)

        ps = [[*p1], [*p2], [*p3], [*p4]]
        ps.sort()
        l2 = dis2(ps[0], ps[1])
        if not l2 or (dis2(ps[0], ps[2]) != l2) or (dis2(ps[3], ps[1]) != l2) or (dis2(ps[3], ps[2]) != l2): return False
        if (ps[1][0] - ps[0][0])*(ps[2][0] - ps[0][0]) + (ps[1][1] - ps[0][1])*(ps[2][1] - ps[0][1]) != 0: return False
        return True


if __name__ == '__main__':
    s = Solution()

    result = True
    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,1]
    print(s.validSquare(p1, p2, p3, p4))

    result = False
    p1 = [0,0]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    print(s.validSquare(p1, p2, p3, p4))

    result = False
    p1 = [0,0]
    p2 = [5,0]
    p3 = [5,4]
    p4 = [0,4]
    print(s.validSquare(p1, p2, p3, p4))
    
        