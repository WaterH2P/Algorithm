n = int(input().strip())
for z in range(n):
    string, subStr = map(str, input().strip().split(','))
    numDel = 0
    indexes = []
    while string.find(subStr) > -1:
        indexes.append(str(string.find(subStr)+numDel))
        numDel += string.find(subStr) + 1
        string = string[string.find(subStr)+1:]
    print(' '.join(indexes))