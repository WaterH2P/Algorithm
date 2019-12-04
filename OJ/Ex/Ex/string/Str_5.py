# Given is a string of length L. 
# Find the longest string from the given string with characters arranged in descending order of their ASCII code and in arithmetic progression.
# She wants the common difference should be as low as possible(at least 1) and the characters of the string to be of higher ASCII value.


for _ in range(int(input().strip())):
    str1 = [(s, ord(s)) for s in input().strip()]
    strT, strM = '', ''
    ASCIIT, ASCIIM = 0, 0
    preASCII = -1
    disASCII = 999
    for item in str1:
        if preASCII == -1:
            preASCII = item[1]
            strT = item[0]
            ASCIIT = item[1]
        elif disASCII == 999:
            disASCII = item[1] - preASCII
            preASCII = item[1]
            strT += item[0]
            ASCIIT += item[1]
        else:
            if disASCII != 0 and disASCII == item[1] - preASCII:
                preASCII = item[1]
                strT += item[0]
                ASCIIT += item[1]
            else:
                if (len(strT) > len(strM)) or (len(strT) == len(strM) and ASCIIT > ASCIIM):
                    strM = strT
                    ASCIIM = ASCIIT
                disASCII = item[1] - preASCII
                strT = strT[-1] + item[0]
                ASCIIT = preASCII + item[1]
                preASCII = item[1]
    if (len(strT) > len(strM)) or (len(strT) == len(strM) and ASCIIT > ASCIIM):
        strM = strT
    print(strM[::-1])
