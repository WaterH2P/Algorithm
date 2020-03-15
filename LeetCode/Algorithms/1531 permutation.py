# 面试题38. 字符串的排列
# 输入一个字符串，打印出该字符串中字符的所有排列。
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

class Solution:
    def permutation(self, s: str) -> List[str]:
        self.res = []
        mem = [*s]
        mem.sort()
        
        def makeup(index, rank, start):
            for i in range(start, len(rank)):
                temp = [*rank]
                temp.insert(i, mem[index])
                if index < len(mem) - 1:
                    if mem[index] == mem[index + 1]:
                        makeup(index+1, [*temp], i+1)
                    else:
                        makeup(index+1, [*temp], 0)
                else:
                    self.res.append(''.join(temp))
            temp = [*rank, mem[index]]
            if index < len(mem) - 1:
                if mem[index] == mem[index + 1]:
                    makeup(index+1, [*temp], len(temp))
                else:
                    makeup(index+1, [*temp], 0)
            else:
                self.res.append(''.join(temp))
        
        makeup(0, [], 0)
        return self.res


if __name__ == "__main__":
    s = Solution()
    strT = "abc"
    print(s.permutation(strT))
                
    strT = "aab"
    print(s.permutation(strT))