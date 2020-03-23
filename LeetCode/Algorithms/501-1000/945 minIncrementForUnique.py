# 【中等】945. 使数组唯一的最小增量
# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
# 返回使 A 中的每个值都是唯一的最少操作次数。

class Solution:
    def minIncrementForUnique(self, A) -> int:
        if len(A) <= 1: return 0
        A.sort()
        count = 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                count += A[i-1] + 1 - A[i]
                A[i] = A[i-1] + 1
        return count


if __name__ == "__main__":
    s = Solution()

    A = [1,2,2]
    print(s.minIncrementForUnique(A))

    A = [3,2,1,2,1,7]
    print(s.minIncrementForUnique(A))
