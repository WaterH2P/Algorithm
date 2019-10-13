def helper(myList, nums, index, length, totalSum, minDiff) :
    if len(myList) == length :
        sum1 = sum(myList)
        sum2 = totalSum - sum(myList)
        diff = abs(sum1 - sum2)
        minDiff = min(minDiff, diff)
        return minDiff
    i = index
    while i < len(nums) :
        myList.append(nums[i])
        minDiff = min(minDiff, helper(myList, nums, i+1, length, totalSum, minDiff))
        myList.pop()
        i += 1
    return minDiff

n = int(input().strip())
for k in range(n) :
    nums1 = list(map(int, input().strip().split()))
    nums2 = list(map(int, input().strip().split()))
    numTotal = [*nums1, *nums2]
    totalSum, length = sum(numTotal), len(nums1)

    myList = []
    minDiff = helper(myList, numTotal, 0, length, totalSum, 9999)
    print(minDiff)