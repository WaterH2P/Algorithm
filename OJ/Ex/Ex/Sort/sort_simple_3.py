# 实现计数排序，通过多次遍历数组，
# 统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。
import sys

for line in sys.stdin:
    if line and len(line) > 1:
        n, *nums = map(int, line.split())
        sCount = [0]*n
        for i in range(n):
            for j in range(n):
                if i != j:
                    numi = nums[i]
                    numj = nums[j]
                    if numi > numj:
                        sCount[i] += 1
                    elif numi == numj and i > j:
                        sCount[i] += 1
        numSort = [0]*n
        for i in range(n):
            index = sCount[i]
            numSort[index] = nums[i]
        print(*numSort, sep=' ')
    else:
        break