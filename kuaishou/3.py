#
# 根据顾客属性计算出顾客排队顺序
# @param a int整型一维数组 顾客a属性
# @param b int整型一维数组 顾客b属性
# @return int整型一维数组
#
class Solution:
    def WaitInLine(self , a , b ):
        if len(a) == 0: return []
        if len(a) == 1: return [1]

        curUnS = 0
        queue = [0]
        for i in range(1, len(a)):
            tmpPre = 0
            if a[i] > b[i]:
                for j in range(0, len(queue) + 1):
                    tmp = curUnS
                    for k in range(0, j): tmp += b[k]
                    for k in range(j, len(queue)): tmp += a[k]
                    tmp += j * a[i] + (len(queue) - j) * b[i]
                    if j == 0:
                        tmpPre = tmp
                        continue
                    if tmp >= tmpPre:
                        queue.insert(j-1, i)
                        curUnS = tmpPre
                        break
                    if j == len(queue):
                        queue.insert(j, i)
                        curUnS = tmp
            else:
                for j in range(len(queue), -1, -1):
                    tmp = curUnS
                    for k in range(0, j): tmp += b[k]
                    for k in range(j, len(queue)): tmp += a[k]
                    tmp += j * a[i] + (len(queue) - j) * b[i]
                    if j == len(queue):
                        tmpPre = tmp
                        continue
                    if tmp >= tmpPre:
                        queue.insert(j+1, i)
                        curUnS = tmpPre
                        break
                    if j == 0:
                        queue.insert(j, i)
                        curUnS = tmp
            # print(queue)
        return [c + 1 for c in queue]


if __name__ == "__main__":
    s = Solution()
    a = [8, 9, 7]
    b = [5, 8, 3]
    print(s.WaitInLine(a, b), '\n')

    a = [1, 1, 1]
    b = [1, 1, 1]
    print(s.WaitInLine(a, b), '\n')

    a = [1, 2, 3, 1]
    b = [1, 2, 1, 1]
    print(s.WaitInLine(a, b), '\n')


                    