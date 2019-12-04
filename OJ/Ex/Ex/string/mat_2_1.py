strA = ['1', '2', '3', '4', '5', '$', '5', '4', '3', '2', '1']  

# 根据 string A 的对称性将 index 转化为 <11 的值
def transIndex(index):
    while index >= 11:
        strLen = len(strA)
        itr = 2
        halfLen = 0
        while index >= strLen:
            if strLen <= index < strLen + itr:
                index = 5
            else:
                halfLen = strLen
                strLen = 2 * strLen + itr
                itr += 1
        if index >= 11:
            dis = index - halfLen - itr
            index = halfLen - dis
    return index
            

for _ in range(int(input().strip())):
    index = int(input().strip())
    index = transIndex(index)
    print(strA[index-1])