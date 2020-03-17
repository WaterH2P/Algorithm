# 【简单】1160. 拼写单词
# 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
# 假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
# 注意：每次拼写时，chars 中的每个字母都只能用一次。
# 返回词汇表 words 中你掌握的所有单词的 长度之和。


class Solution:
    def countCharacters(self, words, chars: str) -> int:
        length = 0
        for word in words:
            for w in word:
                if word.count(w) > chars.count(w):
                    break
            else: length += len(word)
        return length


if __name__ == '__main__':
    s = Solution()

    words = ["cat","bt","hat","tree"]
    chars = "atach"
    print(s.countCharacters(words, chars))