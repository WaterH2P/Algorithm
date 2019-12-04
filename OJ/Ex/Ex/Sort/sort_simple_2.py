# 输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，
# 第一个值为数值长度，其余为数组元素值。
import sys

for line in sys.stdin:
    if line and len(line) > 1:
        n, *nums = list(map(int, line.split()))
        numSort = [*nums]
        isSort = True
        sortNum = 0
        while isSort:
            isSort = False
            for i in range(0, n - 1 - sortNum):
                if numSort[i] > numSort[i + 1]:
                    numSort[i], numSort[i + 1] = numSort[i + 1], numSort[i]
                    isSort = True
            sortNum += 1
        print(*numSort, sep=' ')
    else:
        break