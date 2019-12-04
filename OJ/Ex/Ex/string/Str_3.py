# Given a text txt[0..n-1] and a pattern pat[0..m-1], 
# write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. 
# You may assume that n > m.

for _ in range(int(input().strip())):
    strAll, strSub = input().strip().split(',')
    start = 0
    printStr = ''
    while start <= len(strAll) - len(strSub):
        isSame = True
        for i in range(len(strSub)):
            if strAll[start+i] != strSub[i]:
                isSame = False
                break
        if isSame:
            printStr += str(start) + ' '
        start += 1
    print(printStr[:-1])