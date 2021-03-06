# 1247. 交换字符使得字符串相同
# 有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。
# 每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
# 交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。
# 最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] == 'x':
                xy += 1
            elif s1[i] == 'y':
                yx += 1
        return (xy + 1) // 2 + (yx + 1) // 2 if ((xy + yx) & 1) == 0 else -1

# class Solution:
#     def minimumSwap(self, s1: str, s2: str) -> int:
#         d = collections.Counter(i for i, j in zip(s1, s2) if i != j)
#         if (d['x'] + d['y']) & 1 or len(s1) != len(s2):
#             return -1
#         return sum(divmod(d['x'], 2) + divmod(d['y'], 2))

if __name__ == "__main__":
    s = Solution()

    result = 1
    s1 = "xx"
    s2 = "yy"
    res = s.minimumSwap(s1, s2)
    print(result == res, res, '\n')

    result = 2
    s1 = "xy"
    s2 = "yx"
    res = s.minimumSwap(s1, s2)
    print(result == res, res, '\n')

    result = -1
    s1 = "xx"
    s2 = "xy"
    res = s.minimumSwap(s1, s2)
    print(result == res, res, '\n')

    result = 4
    s1 = "xxyyxyxyxx"
    s2 = "xyyxyxxxyx"
    res = s.minimumSwap(s1, s2)
    print(result == res, res, '\n')

    result = 3
    s1 = "xxxxyyyy"
    s2 = "yyyyxyyx"
    res = s.minimumSwap(s1, s2)
    print(result == res, res, '\n')