# 订单问题
#
# Description:
# Rahul and Ankit are the only two waiters in Royal Restaurant. Today, the restaurant received N orders.
# The amount of tips may differ when handled by different waiters, if Rahul takes the ith order,
# he would be tipped Ai rupees and if Ankit takes this order, the tip would be Bi rupees.In order to
# maximize the total tip value they decided to distribute the order among themselves. One order will
# be handled by one person only. Also, due to time constraints Rahul cannot take more than X orders and
# Ankit cannot take more than Y orders. It is guaranteed that X + Y is greater than or equal to N, which
# means that all the orders can be handled by either Rahul or Ankit. Find out the maximum possible amount
# of total tip money after processing all the orders.
#
# Input:
# 1
# 5 3 3
# 1 2 3 4 5
# 5 4 3 2 1
#
# Output:
# 21

for t in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = [abs(x - y) for x, y in zip(a, b)]
    index = [i for i in range(n)]
    zipped = zip(diff, index)
    z = [x for _, x in sorted(zipped)]

    res = 0
    for i in reversed(z):
        if a[i] >= b[i] and x > 0:
            x = x - 1
            res = res + a[i]
        elif a[i] >= b[i]:
            y = y - 1
            res = res + b[i]
        elif b[i] >= a[i] and y > 0:
            y = y - 1
            res = res + b[i]
        elif b[i] >= a[i]:
            x = x - 1
            res = res + a[i]

    print(res)

