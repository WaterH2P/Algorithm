# 输入第一行为用例个数，每个测试用例输入的每一行代表一个数组，
# 其中的值用空格隔开，第一个值表示数组的长度。

for _ in range(int(input().strip())):
    nums = list(map(int, input().strip().split()))
    nums.pop(0)
    numSort = []
    for num in nums:
        if len(numSort) == 0:
            numSort.append(num)
        else:
            isInsert = False
            for i in range(len(numSort)):
                numT = numSort[i]
                if num < numT:
                    numSort.insert(i, num)
                    isInsert = True
                    break
            if not isInsert:
                numSort.append(num)
    print(*numSort, sep=' ')