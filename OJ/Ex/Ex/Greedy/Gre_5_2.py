t=int(input())
for i in range(0,t):
    m,n=list(map(int,input().split()))
    first=list(map(int,input().split()))
    second=list(map(int,input().split()))
    intersection=[[0,0]]
    f=0
    s=0
    while(True):
        if f>=m or s>=n:
            break
        if first[f]>second[s]:
            s+=1
        elif first[f]<second[s]:
            f+=1
        elif first[f]==second[s]:
            try:
                if first[f+1]==first[f]:
                    f+=1
                    continue
                if second[s+1]==second[s]:
                    s+=1
                    continue
            except:
                pass
            intersection.append([f,s])
            f+=1
            s+=1
    count=0
    f=0
    s=0
    def segcount(intsc0,intsc1=None):
        fcount=0
        scount=0
        if intsc1==None:
            for i in range(intsc0[0],m):
                fcount+=first[i]
            for i in range(intsc0[1],n):
                scount+=second[i]
            return [fcount,scount]
        for i in range(intsc0[0],intsc1[0]):
            fcount+=first[i]
        for i in range(intsc0[1],intsc1[1]):
            scount+=second[i]
        return [fcount,scount]
    for i in range(0,len(intersection)):
        if i+1!=len(intersection):
            result=segcount(intersection[i],intersection[i+1])
        else:
            result=segcount(intersection[i])
        count+=max(result[0],result[1])
    print(count)