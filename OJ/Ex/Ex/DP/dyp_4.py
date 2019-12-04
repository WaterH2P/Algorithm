# Rahul wanted to purchase vegetables mainly brinjal, carrot and tomato. 
# There are N different vegetable sellers in a line. 
# Each vegetable seller sells all three vegetable items, but at different prices. 
# Rahul, obsessed by his nature to spend optimally, decided not to purchase same vegetable from adjacent shops. 
# Also, Rahul will purchase exactly one type of vegetable item (only 1 kg) from one shop. 
# Rahul wishes to spend minimum money buying vegetables using this strategy. 
# Help Rahul determine the minimum money he will spend.

for _ in range(int(input().strip())):
    n = int(input().strip())
    costs = []
    for i in range(n):
        costs.append(list(map(int, input().strip().split())))
    dp = [[0, 0, 0] for i in range(n)]
    for x in range(n):
        for y in range(3):
            if x == 0:
                dp[x][y] = costs[x][y]
            else:
                dpT = [*dp[x-1]]
                dpT.pop(y)
                dp[x][y] = min(*dpT) + costs[x][y]
    print(min(*dp[-1]))