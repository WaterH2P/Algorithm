import itertools
for k in range(int(input().strip())) :
    arr, minDis = [*list(map(int, input().strip().split())), *list(map(int, input().strip().split()))], 999
    print(min( [ abs(sum(arrT)-(sum(arr) - sum(arrT))) for arrT in itertools.combinations(arr, int(len(arr)/2)) ] ))