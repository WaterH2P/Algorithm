# 151. 翻转字符串里的单词
# 给定一个字符串，逐个翻转字符串中的每个单词。


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

if __name__ == '__main__':
    s = Solution()
    strt = 'the sky is blue'
    print(s.reverseWords(strt))

    strt = 'a good   example'
    print(s.reverseWords(strt))
