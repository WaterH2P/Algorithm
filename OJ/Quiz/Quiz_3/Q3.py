A = '12345'
B = '54321'

def f(n, i):
    if i == 1:
        return A[n]
    elif:
        pass


for i in int(input().strip()):
    index = int(input().strip())
    if index <= len(A):
        print(A[index-1])
    elif index <= len(A)+i+1:
        print('$')
    else:
        print(B[index - (len(A)+i+1) - 1])
