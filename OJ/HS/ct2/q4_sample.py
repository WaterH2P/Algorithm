# 一个数有 9 个因数，这个数一定是 p^8 或 p^2*q^2 的形式，其中 p、q 为质数
n = 10 ** 6
prime = [True for i in range(n + 1)]
p = 2
while p * p <= n:
    if prime[p]:
        for i in range(p * 2, n + 1, p):
            prime[i] = False
    p += 1
temp = []

for i in range(2, n + 1):
    if prime[i]:
        temp.append(i)

# print(temp[:10])
t = int(input())
for _ in range(t):
    m = int(input())
    cnt = 0
    i = 0
    while (i < len(temp)):
        j = i + 1
        if (pow(temp[i] * temp[j], 2) > m):
            break
        while (j < len(temp)):
            if (pow(temp[i] * temp[j], 2) > m):
                break
            # print(temp[i],temp[j])
            j += 1
            cnt += 1
        i += 1

    i = 0
    while (temp[i] < 28):
        if (pow(temp[i], 8) > m):
            break
        cnt += 1
        i += 1
    print(cnt)
