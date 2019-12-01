
for _ in range(int(input().strip())):
    numOfCoin, amount = map(int, input().strip().split())
    coinValues = list(map(int, input().strip().split()))
    minCounts = [999]*amount
    for value in coinValues:
        minCounts[value - 1] = 1
    for i in range(amount):
        if minCounts[i] == 999:
            minCount = 999
            for value in coinValues:
                if value <= i:
                    minCount = min(minCount, 1+minCounts[i-value])
            minCounts[i] = minCount
    print(minCounts[-1] if minCounts[-1] != 999 else -1)
