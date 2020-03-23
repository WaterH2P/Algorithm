# 【简单】836. 矩形重叠
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
# 给出两个矩形，判断它们是否重叠并返回结果。


class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        # 判断不重叠
        if rec1[3] <= rec2[1] or rec2[3] <= rec1[1] or rec1[2] <= rec2[0] or rec2[2] <= rec1[0]: return False
        return True 


if __name__ == '__main__':
    s = Solution()

    result = True
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]
    print(s.isRectangleOverlap(rec1, rec2))

    result = False
    rec1 = [0,0,1,1]
    rec2 = [1,0,2,1]
    print(s.isRectangleOverlap(rec1, rec2))

    result = True
    rec1 = [4,4,14,7]
    rec2 = [4,3,8,8]
    print(s.isRectangleOverlap(rec1, rec2))