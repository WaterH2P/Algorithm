# Consider a string A = "12345". 
# An infinite string s is built by performing infinite steps on A recursively. 
# In i-th step, A is concatenated with ‘$’ i times followed by reverse of A. 
# A=A|$...$|reverse(A), where | denotes concatenation.
# Constraints:1<=Q<=10^5, 1<=POS<=10^12

strA = '12345'
numI = 0
for _ in range(int(input().strip())):
    index = int(input().strip())
    while index > len(strA):
        numI += 1
        strA = strA + '$'*numI + strA[::-1]
    print(strA[index-1])
