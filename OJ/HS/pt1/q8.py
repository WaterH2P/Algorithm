from itertools import combinations
for i in range(int(input())):
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    print(min([abs(sum(a+b) - 2 * sum(com)) for com in combinations(a+b, len(a))]))
