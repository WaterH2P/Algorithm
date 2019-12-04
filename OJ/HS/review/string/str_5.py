from collections import Counter
# 和最大的连续降序字符
for _ in range(int(input())):
    arr = list(map(ord, input()))
    arr = list(set(arr))
    arr.sort()
    arr.reverse()
    li = Counter(arr)
    
    start, max_len, gap = 0, 0, 0
    for i in range(1,13):
        for j in range(len(arr)):
            cur_len = 1
            a = arr[j]
            while li[a-i]>0:
                a -= i
                cur_len += 1
            if cur_len > max_len:
                gap, max_len, start = i, cur_len, arr[j]
                
    for i in range(0, max_len):
        print(chr(start),end='')
        start -= gap
    
    print()