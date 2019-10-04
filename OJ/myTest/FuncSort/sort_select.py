def sort_select(l):
    minI, index, maxI = 0, 0, len(l)
    while index < maxI :
        minI = i = index
        while i < maxI :
            if l[minI] > l[i] :
                minI = i
            i += 1
        l[index], l[minI] = l[minI], l[index]
        index += 1
    return l
    
L = [2, 5, 7, 1, 4, 3, 0]
L2 = sort_select(L)
print(L2)