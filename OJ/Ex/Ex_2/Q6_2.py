def count_sort(list):
    count_list = [0] * len(list)
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if i == j:
                continue
            else:
                if list[i] > list[j]:
                    count_list[i] += 1
    # print(count_list)
    new_list = [-1] * len(count_list)
    for k in range(len(count_list)):
        if new_list[count_list[k]] == -1:
            new_list[count_list[k]] = list[k]
            # print(new_list)
        else:
            key = list[k]
            index = count_list[k]+1
            # print(key, index)
            while index < len(new_list):
                if new_list[index] == -1:
                    break
                index += 1
            new_list[index] = key
    return new_list

import sys
for line in sys.stdin:
    intlist = list(map(int, line.strip().split()))
    del intlist[0]
    intlist = count_sort(intlist)
    strlist = [str(x) for x in intlist]
    print(' '.join(strlist))
