
import math

def sort_merge(l, r):
    if len(l) < 2 :
        return l, r
    else :
        mid = math.floor( len(l)/2 )
        l1 = l[:mid]
        l2 = r[:mid]
        r1 = l[mid:]
        r2 = r[mid:]
        left1, left2 = sort_merge(l1, l2)
        right1, right2 = sort_merge(r1, r2)
        return merge(left1, left2, right1, right2)

def merge(l1, l2, r1, r2):
    res = []
    res2 = []
    i = j = 0
    while i < len(l1) and j < len(r1) :
        if l1[i] < r1[j] :
            res.append(l1[i])
            res2.append(l2[i])
            i += 1
        else :
            res.append(r1[j])
            res2.append(r2[j])
            j += 1
    while i < len(l1) :
        res.append(l1[i])
        res2.append(l2[i])
        i += 1
    while j < len(r1) :
        res.append(r1[j])
        res2.append(r2[j])
        j += 1
    return res, res2

n = int( input().strip() )
while n > 0 :
    myDict = {}
    length = int( input().strip() )
    nums = list( map(int, input().strip().split()) )
    if len(nums) > length :
        nums = nums[:length]
    i = 0
    while i < len(nums) :
        num = nums[i]
        if num in myDict.keys():
            myDict[num] += 1
        else :
            myDict[num] = 1
        i += 1
    count = [x for x in myDict.items()]
    count.sort(reverse = True, key = lambda x: (x[1], -x[0]))
    i = 0
    output = ''
    while i < len(count) :
        j = (count[i])[1]
        while j > 0 :
            output += str((count[i])[0]) + ' '
            j -= 1
        i += 1
    print(output.strip())
    n -= 1