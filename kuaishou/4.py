#
# 获取最大可同事办公员工数
# @param pos char字符型二维数组 工位分布
# @return int整型
#
class Solution:
    def GetMaxStaffs(self , pos):
        self.maxSeat = 0
        self.length = len(pos[0])

        for i in range(len(pos)):
            for j in range(len(pos[0])):
                pos[i][j] = 1 if pos[i][j] == '.' else 0
        pos = [int(''.join(map(str, seat)), 2) for seat in pos]
        
        def set(pos, curSeat):
            # print(pos)
            # print(curSeat)
            while len(pos) > 1 and pos[0] == 0: pos.pop(0)
            if len(pos) == 1:
                curSeat += bin(pos[0])[2:].count('1')
                if curSeat > self.maxSeat: self.maxSeat = curSeat
                return
            line1 = bin(pos[0])[2:]
            line1 = '0' * (self.length - len(line1)) + line1
            line1 = list(map(int, [_ for _ in line1]))
            line2 = bin(pos[1])[2:]
            line2 = '0' * (self.length - len(line2)) + line2
            line2 = list(map(int, [_ for _ in line2]))

            # print(line1)
            # print(line2)
            # print()

            for i in range(len(line1)):
                tmpCurSeat = curSeat
                if line1[i] == 1:
                    tmp1 = [_ for _ in line1]
                    tmp2 = [_ for _ in line2]
                    tmpCurSeat += 1
                    tmp1[i] = 0
                    if i > 0: tmp1[i-1] = 0
                    if i < len(tmp1) - 1: tmp1[i+1] = 0
                    tmp2[i] = 0
                    posT = [int(''.join(map(str, tmp1)), 2), int(''.join(map(str, tmp2)), 2), *pos[2:]]
                    set(posT, tmpCurSeat)
            return
        set(pos, 0)
        return self.maxSeat


if __name__ == "__main__":
    s = Solution()
    # pos = [
    #     ['*', '.', '*', '*', '.'],
    #     ['*', '.', '*', '*', '*'],
    #     ['*', '.', '*', '*', '.'],
    # ]
    # print(s.GetMaxStaffs(pos) == 4)

    pos = [
        ['*', '.', '*', '*', '.'],
        ['*', '.', '*', '.', '.'],
        ['*', '.', '*', '*', '.'],
    ]
    print(s.GetMaxStaffs(pos) == 5)

    # pos = [
    #     ['*', '*'],
    #     ['*', '*'],
    # ]
    # print(s.GetMaxStaffs(pos) == 0)

    # pos = [
    #     ['*'],
    #     ['.'],
    # ]
    # print(s.GetMaxStaffs(pos) == 1)

    # pos = [
    #     ['.'],
    #     ['.'],
    # ]
    # print(s.GetMaxStaffs(pos) == 1)

    # pos = [
    #     ['.'],
    # ]
    # print(s.GetMaxStaffs(pos) == 1)

    # pos = [
    #     ['*'],
    # ]
    # print(s.GetMaxStaffs(pos) == 0)