#
# 返回无重复幂因子的 N进制完美数之和的所有幂因子
# @param R int整型 
# @param N int整型 N进制
# @return int整型一维数组
#
class Solution:
    def GetPowerFactor(self , R , N):
        self.res = []

        def find(R, N):
            if R == 0: return
            else:
                m = 0
                while pow(N, m) <= R: m += 1
                m -= 1
                if m not in self.res:
                    self.res.append(m)
                    R -= pow(N, m)
                    find(R, N)
                else:
                    self.res = []
            return
        
        find(R, N)
        self.res.sort()
        return self.res


if __name__ == "__main__":
    s = Solution()
    R = 39
    N = 3
    print(s.GetPowerFactor(R, N))

    R = 33
    N = 3
    print(s.GetPowerFactor(R, N))