# 【中等】1453. 面试题 10.02. 变位词组
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。


class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for word in strs:
            strT = str(sorted(word))
            if strT in res: res[strT].append(word)
            else: res[strT] = [word]
        return list(res.values())


if __name__ == '__main__':
    s = Solution()

    result = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(result))