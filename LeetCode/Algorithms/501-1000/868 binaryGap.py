# 868. 二进制间距
# 给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。 
# 如果没有两个连续的 1，返回 0 。


class Solution:
    def binaryGap(self, N: int) -> int:
        gaps = [len(_) for _ in bin(N)[2:].split('1')[1:-1]]
        return max(gaps) + 1 if len(gaps) > 0 else 0

if __name__ == "__main__":
    s = Solution()

    result = 2
    n = 22
    print(s.binaryGap(n))

    result = 2
    n = 5
    print(s.binaryGap(n))

    result = 1
    n = 6
    print(s.binaryGap(n))

    result = 0
    n = 8
    print(s.binaryGap(n))