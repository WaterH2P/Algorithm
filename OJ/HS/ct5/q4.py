import sys
for t in range(int(input())):
    n, amount = map(int, input().split())
    coins = list(map(int, input().split()))
    table = [0 for i in range(amount + 1)]
    table[0] = 0
    for i in range(1, amount + 1):
        table[i] = sys.maxsize
    for i in range(1, amount + 1):
        for j in range(n):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1
    print(table[amount]) if table[amount] != sys.maxsize else print(-1)
