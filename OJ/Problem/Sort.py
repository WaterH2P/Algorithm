n = int(input().strip())
for k in range(n) :
    count, length, arr = [], int(input().strip()), list(map(int, input().strip().split()))
    for val in arr :
        isExist = False
        for arrT in count :
            if val == arrT[0] :
                arrT[1] += 1
                isExist = True
                break
        if not isExist :
            count.append([val, 1])
    count.sort(reverse=True, key=lambda x: (x[1], -x[0]))
    output = ''
    for arrT in count :
        for i in range(arrT[1]) :
            output += str(arrT[0]) + ' '
    print(output.strip())