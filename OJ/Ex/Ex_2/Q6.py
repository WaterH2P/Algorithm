
# 计数排序
def countSort(nums):
    numSort = [None]*len(nums)
    for num1 in nums:
        l, r = 0, 0
        for num2 in nums:
            if num1 > num2:
                l += 1
            elif num1 == num2:
                r += 1
        for i in range(l, l+r):
            numSort[i] = num1
    return numSort


import sys
for nums in sys.stdin:
    nums = list(map(int, nums.split(' ')))
    length = nums.pop(0)
    nums.sort()
    nums = list(map(str, nums))
    print(' '.join(nums))
    nums = input().strip()
