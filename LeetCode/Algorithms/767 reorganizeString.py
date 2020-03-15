# 767. 重构字符串
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
# 若可行，输出任意可行的结果。若不可行，返回空字符串。


class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) == 1: return S
        counts = {}
        for s in S:
            if s in counts: counts[s] += 1
            else: counts[s] = 1
        counts = [[counts[ele], ele] for ele in counts]
        mostEle = counts.pop(0)
        for i in range(len(counts)):
            if counts[i][0] > mostEle[0]:
                mostEle, counts[i] = counts[i], mostEle
        if 2 * mostEle[0] > len(S) + 1: return ''
        eles = []
        for i in range(len(counts)):
            for j in range(0, counts[i][0]):
                eles.append(counts[i][1])
        i, j, res = 1, 0, [mostEle[1] for _ in range(mostEle[0])]
        while j < len(eles):
            res.insert(i, eles[j])
            i += 2
            j += 1
            if i == len(res) + 1: i = 1
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()

    S = 'aab'
    print(s.reorganizeString(S))

    S = 'aaab'
    print(s.reorganizeString(S))

    S = 'vvvlo'
    print(s.reorganizeString(S))