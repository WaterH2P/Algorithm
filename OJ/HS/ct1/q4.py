t = int(input())
while t != 0:
    t -= 1
    length = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res = sorted(arr1)
    my_rule = dict()
    for index, value in enumerate(arr2):
        my_rule[value] = index

    def my_sort(v):
        if v in my_rule:
            return my_rule[v]
        else:
            return length[1]

    res = sorted(res, key=my_sort)
    print(*res)
