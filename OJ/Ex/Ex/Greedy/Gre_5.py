# There are two parallel roads, each containing N and M buckets, respectively. 
# Each bucket may contain some balls. 
# The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them. 
# Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. 
# if buckets are sorted in increasing order, then geek will start from the left side of the road). 
# The geek can change the road only at the point of intersection(which means, buckets with the same number of balls on two roads). 
# Now you need to help Geek to collect the maximum number of balls.

for _ in range(int(input().strip())):
    n, m = map(int, input().strip().split())
    roadNT = list(map(int, input().strip().split()))
    roadNT.sort()
    roadMT = list(map(int, input().strip().split()))
    roadMT.sort()
    roadN = [[roadNT[0], 1]]
    roadM = [[roadMT[0], 1]]
    for i in range(1, n):
        if roadNT[i] == roadN[-1][0]:
            roadN[-1][1] += 1
        else:
            roadN.append([roadNT[i], 1])
    for j in range(1, m):
        if roadMT[j] == roadM[-1][0]:
            roadM[-1][1] += 1
        else:
            roadM.append([roadMT[j], 1])
    n, m = len(roadN), len(roadM)
    cN, cM = 0, 0
    i, j = 0, 0
    while i < n and j < m:
        if roadN[i][0] < roadM[j][0]:
            cN += roadN[i][0] * roadN[i][1]
            i += 1
        elif roadN[i][0] > roadM[j][0]:
            cM += roadM[j][0] * roadM[j][1]
            j += 1
        elif roadN[i][0] == roadM[j][0]:
            cN += roadN[i][0] * (roadN[i][1] + roadM[j][1] - 1)
            cM += roadM[j][0] * (roadN[i][1] + roadM[j][1] - 1)
            cN = max(cN, cM)
            cM = cN
            i += 1
            j += 1
    for k in range(i, n):
        cN += roadN[i][0] * roadN[i][1]
    for k in range(j, m):
        cM += roadM[j][0] * roadM[j][1]
    print(max(cN, cM))