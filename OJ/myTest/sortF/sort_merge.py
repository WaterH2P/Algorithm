import math

def sort_merge(l):
    if len(l) < 2 :
        return l
    else :
        mid = math.floor( len(l)/2 )
        left = l[:mid]
        right = l[mid:]
        return merge(sort_merge(left), sort_merge(right))

def merge(l, r):
    res = []
    i = j = 0
    while i < len(l) and j < len(r) :
        if l[i] < r[j] :
            res.append(l[i])
            i += 1
        else :
            res.append(r[j])
            j += 1
    while i < len(l) :
        res.append(l[i])
        i += 1
    while j < len(r) :
        res.append(r[j])
        j += 1
    return res

L = [2, 5, 7, 1, 4, 3, 0]
L2 = sort_merge(L)
print(L2)