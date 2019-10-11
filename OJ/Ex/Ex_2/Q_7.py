def incrList(arr):
    if len(arr) == 0 :
        return []
    arrTs = [[arr[0]]]
    index = 1
    while index < len(arr) :
        indexArr = 0
        while indexArr < len(arrTs) :
            arrT = arrTs[indexArr]
            newArr = []
            if arr[index] < arrT[0] :
                newArr = [arr[index]]
            elif arr[index] > arrT[-1] :
                newArr = [*arrT, arr[index]]
            if len(newArr) > 0 :
                arrTs.insert(indexArr+1, newArr)
                indexArr += 1
            indexArr += 1
        index += 1
    arrTs = listsDistinct(arrTs)
    return arrTs

def maxLenList(arr):
    maxLen = 0
    index = 0
    while index < len(arr) :
        if len(arr[index]) > maxLen :
            maxLen = len(arr[index])
            arr = arr[index:]
            index = 0
        elif len(arr[index]) < maxLen :
            arr.pop(index)
            index -= 1
        index += 1
    return arr

def joinList(arr, arrIn):
    joinLists = []
    maxLen = 0
    for arrl in arrIn :
        index, il = 0, 0
        while index < len(arr) and il < len(arrl) :
            if arr[index] == arrl[il] :
                il += 1
            index += 1
        if il == len(arrl) and index < len(arr) :
            arrR = arr[index:]
            if len(arrR) > 0 :
                arrR.reverse()
            arrRDecrList = incrList(arrR)
            arrRMaxDecrList = maxLenList(arrRDecrList)
            for arrT in arrRMaxDecrList :
                arrT.reverse()
            if len(arrRMaxDecrList) == 0 :
                if len(arrl) > maxLen :
                    joinLists = [arrl]
                    maxLen = len(arrl)
                elif len(arrl) == maxLen :
                    joinLists.append(arrl)
            else :
                if len(arrl) + len(arrRMaxDecrList[0]) > maxLen :
                    joinLists = []
                    for arrT in arrRMaxDecrList :
                        joinLists.append([*arrl, *arrT])
                    maxLen = len(arrl) + len(arrRMaxDecrList[0])
                elif len(arrl) + len(arrRMaxDecrList[0]) == maxLen :
                    for arrT in arrRMaxDecrList :
                        joinLists.append([*arrl, *arrT])
        elif il == len(arrl) and index == len(arr) :
            if len(arrl) > maxLen :
                joinLists = [arrl]
                maxLen = len(arrl)
            elif len(arrl) == maxLen :
                joinLists.append(arrl)
    joinLists = listsDistinct(joinLists)
    return joinLists

def listsDistinct(arrs):
    return [list(t) for t in set(tuple(_) for _ in arrs)]

n = int(input().strip())
for k in range(n) :
    arr = list(map(int, input().strip().split()))
    arrIn = incrList(arr)
    joinLists = joinList(arr, arrIn)
    strJoinLists = []
    for arrT in joinLists :
        strOutput = ''.join([str(x) + ' ' for x in arrT])
        strJoinLists.append(strOutput.strip())
    strJoinLists.sort()
    for strOutput in strJoinLists :
        print(strOutput)