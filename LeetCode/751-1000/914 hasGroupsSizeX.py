# 【简答】914. 卡牌分组
# 给定一副牌，每张牌上都写着一个整数。
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 仅当你可选的 X >= 2 时返回 true。


import collections

class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        if len(deck) <= 1: return False
        mem = collections.Counter(deck)
        minerNum = minNum = float('inf')
        
        for num in mem:
            if mem[num] < minerNum: minNum, minerNum = minerNum, mem[num]
            elif mem[num] < minNum and mem[num] > minerNum: minNum = mem[num]

        if minNum == float('inf'): minNum = minerNum
        while minerNum != 0: minNum, minerNum = minerNum, minNum % minerNum

        if minNum < 2: return False
        for num in mem:
            if mem[num] % minNum != 0:
                print(mem[num])
                return False
        return True


if __name__ == '__main__':
    s = Solution()

    # result = True
    # deck = [1,2,3,4,4,3,2,1]
    # print(s.hasGroupsSizeX(deck))

    # result = False
    # deck = [1,1,1,2,2,2,3,3]
    # print(s.hasGroupsSizeX(deck))

    # result = True
    # deck = [1,1]
    # print(s.hasGroupsSizeX(deck))

    # result = True
    # deck = [0,0,0,0,0,0]
    # print(s.hasGroupsSizeX(deck))

    # result = True
    # deck = [1,1,1,1,2,2,2,2,2,2]
    # print(s.hasGroupsSizeX(deck))