class Solution:
    def combinationSum(self, candidates, target: int):
        res, i = [], 0
        while i < len(candidates):
            if candidates[i] >= target:
                if candidates[i] == target:
                    res.append([target])
                candidates.pop(i)
                i -= 1
            i += 1
        

if __name__ == '__main__':
    s = Solution()            