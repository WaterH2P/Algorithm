inp = input()
strls = inp.strip().split()
ls = list(map(int, strls))
del ls[0]
for index in range(1, len(ls)):
    for j in range(0, index):
        # print(ls[j], ls[index])
        if ls[j] > ls[index]:
            tmp = ls[index]
            ls[index] = ls[j]
            ls[j] = tmp
    # print('===', ls)
strls = [str(x) for x in ls]
print(' '.join(strls))