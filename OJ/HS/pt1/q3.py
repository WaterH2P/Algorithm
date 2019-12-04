for i in range(int(input())):
    arr, w = list(map(int, input().split())), int(input())
    print(sum(map(max, zip(*[arr[i:] for i in range(w)]))))
