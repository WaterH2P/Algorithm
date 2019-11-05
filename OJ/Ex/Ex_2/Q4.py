
# 插入排序
def insertSort(nums):
    numSort = [nums[0]]
    for num in nums[1:]:
        i = 0
        while i < len(numSort):
            if num < numSort[i]:
                numSort.insert(i, num)
                break
            if i == len(numSort) - 1:
                numSort.append(num)
                break
            i += 1
    return numSort


for z in range(int(input().strip())):
    nums = list(map(int, input().strip().split(' ')))
    length = nums.pop(0)
    nums = insertSort(nums)
    numOutput = [str(num) for num in nums]
    print(' '.join(numOutput))
