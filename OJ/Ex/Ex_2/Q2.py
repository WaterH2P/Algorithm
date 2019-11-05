
for z in range(int(input().strip())):
    strs = input().strip().split(' ')
    length = int(strs.pop(0))
    i, j = 0, length - 1
    ifHuiWen = True
    while j > i and ifHuiWen:
        if not strs[i] == strs[j]:
            ifHuiWen = False
            break
        i += 1
        j -= 1
    if ifHuiWen:
        print('true')
    else:
        print('false')