for t in range(int(input())):
    length = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res, unsort = [], []
    [res.append(i) for i in arr2 for j in arr1 if j == i]
    [unsort.append(j) for j in arr1 if j not in arr2]
    res.extend(sorted(unsort))
    print(*res)
    
    # res = sorted(arr1)
    # my_rule = dict()
    # for index, value in enumerate(arr2):
    #     my_rule[value] = index

    # def my_sort(v):
    #     if v in my_rule:
    #         return my_rule[v]
    #     else:
    #         return length[1]

    # res = sorted(res, key=my_sort)
    # print(*res)

