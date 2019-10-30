n = int(input().strip())
for k in range(n) :
    arr = list( map(int, input().strip().split()) )
    w = int(input().strip())
    first, sumVal = 0, 0
    while first + w <= len(arr) :
        sumVal += max(arr[first:first+w])
        first += 1
    print(sumVal)