import math

def sort_shell(l):
    maxI = len(l)
    gap = math.floor(maxI/2)
    while gap > 0 :
        j = gap
        while j < maxI :
            i = j
            current = l[i]
            while i - gap > -1 and current < l[i-gap]:
                l[i], l[i-gap] = l[i-gap], l[i]
                i -= gap
            j += 1
            i = j
        gap = math.floor(gap/2)
    return l

L = [2, 5, 7, 1, 4, 3, 0]
L2 = sort_shell(L)
print(L2)