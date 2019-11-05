
# 冒泡排序
def bubbleSort(nums):
    numSort = [num for num in nums]
    numsLen = len(numSort)
    isChange = True
    while numsLen > 1 and isChange:
        isChange = False
        for i in range(numsLen-1):
            if numSort[i] > numSort[i+1]:
                numSort[i], numSort[i+1] = numSort[i+1], numSort[i]
                isChange = True
        numsLen -= 1
    return numSort


nums = list(map(int, input().strip().split(' ')))
length = nums.pop(0)
nums = bubbleSort(nums)
nums = list(map(str, nums))
print(' '.join(nums))
