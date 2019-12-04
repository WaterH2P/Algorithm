import sys
for line in sys.stdin:
    n, *arr = list(map(int, line.split()))
    l, r = 0, n-1
    stack = list()
    stack.append(l)
    stack.append(r)
    while len(stack):
        r = stack.pop()
        l = stack.pop()
        if l < r:
            pivot = arr[l]
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= pivot:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    break
                while i < j and arr[i] <= pivot:
                    i += 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    break
            mid = i
            # left
            stack.append(l)
            stack.append(mid-1)
            # right
            stack.append(mid+1)
            stack.append(r)
    print(*arr)
