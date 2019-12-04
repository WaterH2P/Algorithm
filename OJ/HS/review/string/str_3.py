# 字符串匹配问题
for t in range(int(input())):
    arr, query = input().split(',')
    res, start = [], 0
    while True:
        try:
            pos = arr.index(query, start)
            res.append(pos)
            start = pos + 1
        except:
            break
    print(*res)