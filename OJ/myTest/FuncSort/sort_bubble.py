def sort_bubble(l):
    max = len(l)
    while max > 0 :
        a, b = 0, 1
        while b < max :
            if l[a] > l[b] :
                l[a], l[b] = l[b], l[a]
            a, b = b, b+1
        max -= 1
    return l

L = [2, 5, 7, 1, 4, 3, 0]
L2 = sort_bubble(L)
print(L2)