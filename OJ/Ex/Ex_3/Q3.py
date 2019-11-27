
# 该方法实质上是一种分组插入方法

# 插入排序
def insertSort(nums):
    numsSort = []
    for num in nums:
        if len(numsSort) == 0:
            numsSort.append(num)
        else:
            if num > numsSort[-1]:
                numsSort.append(num)
                continue
            for i in range(len(numsSort)):
                numT = numsSort[i]
                if numT >= num:
                    numsSort.insert(i, num)
                    break
    return numsSort

for _ in range(int(input().strip())):
    nums = list(map(int, input().strip().split()))
    intervals = list(map(int, input().strip().split()))
    for interval in intervals:
        for start in range(interval):
            index = start
            indexs = []
            while index < len(nums):
                indexs.append(index)
                index += interval
            numsT = []
            for index in indexs:
                numsT.append(nums[index])
            numsT = insertSort(numsT)
            i = 0
            for index in indexs:
                nums[index] = numsT[i]
                i += 1
    print(*nums, sep=' ')