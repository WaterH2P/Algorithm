# Given an array of strings A[ ], determine if the strings can be chained together to form a circle. 
# A string X can be chained together with another string Y if the last character of X is same as first character of Y. 
# If every string of the array can be chained, it will form a circle. 
# For example, for the array arr[] = {"for", "geek", "rig", "kaf"} 
# the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf".

# https://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-form-circle/

for _ in range(int(input().strip())):
    strNum = int(input().strip())
    strs = [s[0] + s[-1] for s in input().strip().split()]
    charl, charr, oneChar = {}, {}, []

    i = 0
    while i < len(strs):
        item = strs[i]
        if item[0] == item[1]:
            if item[0] not in oneChar:
                oneChar.append(item[0])
            strs.pop(i)
            i -= 1
        i += 1

    if len(oneChar) == 1 and len(strs) == 0:
        print('1')
        continue

    for item in strs:
        charl[item[0]] = 1 if item[0] not in charl else charl[item[0]] + 1
        charr[item[1]] = 1 if item[1] not in charr else charr[item[1]] + 1
    if len(charl) != len(charr):
        print('0')
    else:
        isCircle = True
        for c in oneChar:
            if c not in charl:
                isCircle = False
                break
        if isCircle:
            for c in charl:
                if c not in charr or charl[c] != charr[c]:
                    isCircle = False
                    break
        print('1' if isCircle else '0')
