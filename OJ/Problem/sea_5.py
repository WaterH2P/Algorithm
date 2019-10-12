n = int(input().strip())
for k in range(n) :
    A1len, A2len = map(int, input().strip().split())
    A1 = list(map(int, input().strip().split()))
    A2 = list(map(int, input().strip().split()))
    arr = []
    for x in A2 :
        index = -1
        if x in A1 :
            index = A1.index(x)
        else :
            continue
        while True :
            arr.append(x)
            A1.pop(index)
            if x in A1 :
                index = A1.index(x)
            else :
                break
    A1.sort()
    arr = [*arr, *A1]
    output = ' '.join([str(x) for x in arr])
    print(output)