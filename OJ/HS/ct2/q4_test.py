limit = 10**6
prime_flag = [True for i in range(limit+1)]
p = 2
while p * p <= limit:
    if prime_flag[p]:
        for i in range(p+p, limit+1, p):
            prime_flag[i] = False
    p += 1
prime = [i for i in range(2, limit+1) if prime_flag[i]]

for t in range(int(input())):
    n = int(input())
    i = 0
    count = 0
    while i < len(prime):
        j = i + 1
        if (prime[i] * prime[j]) ** 2 > n:
            break
        while j < len(prime):
            if (prime[i] * prime[j]) ** 2 > n:
                break
            j += 1
            count += 1
        i += 1
    i = 0
    # while prime[i] < 28:
    #     if pow(prime[i], 8) > n:
    #         break
    #     count += 1
    #     i += 1
    while i < len(prime):
        if prime[i] ** 8 > n:
            break
        count += 1
        i += 1
    print(count)


