def sort_insert(l):
    index, maxI = 0, len(l)
    while index < maxI - 1 :
        i = index + 1
        while i > 0 and l[i] < l[i-1] :
            l[i], l[i-1] = l[i-1], l[i]
            i -= 1
        index += 1
    return l

L = [2, 5, 7, 1, 4, 3, 0]
L2 = sort_insert(L)
print(L2)