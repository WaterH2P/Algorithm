# 最长公共子序列
# for t in range(int(input())):
#     arr1, arr2 = input(), input()
#     m, n = len(arr1), len(arr2)
#     if arr1 in arr2:
#         print(arr1)
#         continue
#     if arr2 in arr1:
#         print(arr2)
#         continue
#     dp = [[['']] * (n+1) for _ in range(m+1)]
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if arr1[i-1] == arr2[j-1]:
#                 dp[i][j] = []
#                 tmp = set([*dp[i-1][j], *dp[i][j-1]]) - set([''])
#                 if not len(tmp):
#                     dp[i][j] = [arr1[i-1]]
#                 else:
#                     for s in tmp:
#                         dp[i][j].append(s + arr1[i-1])
#             else:
#                 if len(dp[i-1][j][0]) == len(dp[i][j-1][0]):
#                     tmp = set([*dp[i-1][j], *dp[i][j-1]])
#                     dp[i][j] = list(tmp)
#                 else:
#                     dp[i][j] = max([*dp[i-1][j]], [*dp[i][j-1]], key=lambda a: len(a[0]))
#     print(*dp, sep='\n')
#     res = dp[-1][-1]
#     if '' in res:
#         continue
#     res.sort()
#     for _ in res:
#         print(_)



# for t in range(int(input())):
#     # arr1, arr2 = list(input()), list(input())
#     s1,s2 = input(), input()
#     n,m = len(s1),len(s2)
#     dp = [[0]*(m+1) for i in range(n+1)]
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if s1[i-1]==s2[j-1]:
#                 dp[i][j] = 1 + dp[i-1][j-1]
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#     ans = [""]
#     def printlcs(currstr,currlcs,i,j):
#         if currlcs == dp[n][m]:
#             ans[0] += "".join(currstr)+" "
#             return
#         if i==n or j==m: return
#         for ch in range(128):
#             done = False
#             for x in range(i,n):
#                 if chr(ch)==s1[x]:
#                     for y in range(j,m):
#                         if chr(ch)==s2[y] and dp[x+1][y+1]==currlcs+1:
#                             currstr.append(chr(ch))
#                             printlcs(currstr,currlcs+1,x+1,y+1)
#                             currstr.pop()
#                             done = True
#                             break
#                 if done: break
#     printlcs([],0,0,0)
#     res = ans[0].split()
#     res.sort()
#     for _ in res:
#         print(_)



def LCS(a, b, memo, i, j):
    la=len(a)
    lb=len(b)
    if i>=la or j>=lb:
        memo[i][j]=0
        return 0
    if memo[i][j]!=-1:
        return memo[i][j]
    
    if a[i]==b[j]:
        memo[i][j]=1+LCS(a,b,memo,i+1,j+1)
        return memo[i][j]
    else:
        memo[i][j]=max(LCS(a,b,memo,i+1,j),LCS(a,b,memo,i,j+1))
        return memo[i][j]

res=[]
def printall(a,b,data,i,j,currlcs,glcs,memo):
    tmp = ''
    if currlcs==glcs:
        data[currlcs]=None
        for it in range(currlcs) :
            tmp+=data[it]
        res.append(tmp)
        return
    if i>=len(a) or j>=len(b):
        return
    for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
        done=False
        for indx1 in range(i,len(a)):
            if a[indx1]==c:
                for indx2 in range(j,len(b)):
                    if b[indx2]==c:
                        if (LCS(a,b,memo,indx1,indx2)==glcs-currlcs):
                            data[currlcs]=c
                            printall(a,b,data,indx1+1,indx2+1,currlcs+1,glcs,memo)
                            done=True
                            break
            if done:
                break
    
        
t=int(input())
while t:
    a,b=input(),input()
    a=str(a)
    b=str(b)
    memo=[[ -1 for j in range(len(b)+1)] for i in range(len(a)+1)]
    lcs=LCS(a,b,memo,0,0)
    data=['' for _ in range(101)]
    printall(a,b,data,0,0,0,lcs,memo)
    res.sort()
    for _ in res: print(_)
    t-=1
