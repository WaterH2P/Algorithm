# 638. 大礼包
# 在LeetCode商店中， 有许多在售的物品。
# 然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
# 现给定每个物品的价格，每个大礼包包含物品的清单，以及待购物品清单。请输出确切完成待购清单的最低花费。
# 每个大礼包的由一个数组中的一组数据描述，最后一个数字代表大礼包的价格，其他数字分别表示内含的其他种类物品的数量。
# 任意大礼包可无限次购买。


# dp 超出时间限制
# class Solution:
#     def shoppingOffers(self, price, special, needs) -> int:
#         dp = [[[[[[None for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)] for _ in range(7)]
#         for i in range(len(price)):
#             gift = [0] * (len(price) + 1)
#             gift[i], gift[-1] = 1, price[i]
#             special.append(gift)
#         for gift in special:
#             a, b, c, d, e, f = [*gift[:-1], 0, 0, 0, 0, 0, 0][:6]
#             if dp[a][b][c][d][e][f] is None or dp[a][b][c][d][e][f] > gift[-1]:
#                 dp[a][b][c][d][e][f] = gift[-1]
#         while len(needs) < 6: needs.append(0)
#         for ai in range(0, needs[0]+1):
#             for bi in range(0, needs[1]+1):
#                 for ci in range(0, needs[2]+1):
#                     for di in range(0, needs[3]+1):
#                         for ei in range(0, needs[4]+1):
#                             for fi in range(0, needs[5]+1):
#                                 for gift in special:
#                                     a, b, c, d, e, f = [*gift[:-1], 0, 0, 0, 0, 0, 0][:6]
#                                     if ai >= a and bi >= b and ci >= c and di >= d and ei >= e and fi >= f:
#                                         if dp[ai][bi][ci][di][ei][fi] is None or (dp[ai-a][bi-b][ci-c][di-d][ei-e][fi-f] is not None and dp[a][b][c][d][e][f] + dp[ai-a][bi-b][ci-c][di-d][ei-e][fi-f] < dp[ai][bi][ci][di][ei][fi]):
#                                             dp[ai][bi][ci][di][ei][fi] = dp[a][b][c][d][e][f] + dp[ai-a][bi-b][ci-c][di-d][ei-e][fi-f]
#         if dp[needs[0]][needs[1]][needs[2]][needs[3]][needs[4]][needs[5]] is not None:
#             return dp[needs[0]][needs[1]][needs[2]][needs[3]][needs[4]][needs[5]]
#         else: return 0


# 回溯 + 剪枝 + 记忆化
class Solution:
    def shoppingOffers(self, price, special, needs) -> int:
        l, mem = len(price), {}

        def shopping(special, needs):
            keyNeeds = str(needs)
            if keyNeeds in mem: return mem[keyNeeds]
            # 删除 special 中某件商品数量超过 needs
            special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(l)), special))
            if not special: return sum([needs[i] * price[i] for i in range(l)])
            minRes = float("inf")
            for gift in special:
                res = gift[-1] + shopping(special, [needs[i] - gift[i] for i in range(l)])
                if res < minRes: minRes = res
            mem[keyNeeds] = minRes
            return minRes
        
        special = list(filter(lambda x: x[-1] < sum(x[i] * price[i] for i in range(l)), special))
        return shopping(special, needs)


s = Solution()
result  = 14
price   = [2,5]
special = [[3,0,5],[1,2,10]]
needs   = [3,2]
print(s.shoppingOffers(price, special, needs))

result  = 11
price   = [2,3,4]
special = [[1,1,0,4], [2,2,1,9]]
needs   = [1,2,1]
print(s.shoppingOffers(price, special, needs))

result  = 0
price   = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs   = [0,0,0]
print(s.shoppingOffers(price, special, needs))

result  = 0
price   = [0,0,0]
special = [[1,1,0,4],[2,2,1,9]]
needs   = [1,1,1]
print(s.shoppingOffers(price, special, needs))

result  = 6
price   = [9,9]
special = [[1,1,1]]
needs   = [6,6]
print(s.shoppingOffers(price, special, needs))

result  = 6
price   = [3,4]
special = [[1,2,3],[1,2,5]]
needs   = [2,2]
print(s.shoppingOffers(price, special, needs))

price   = [9,6,1,5,3,4]
special = [[1,2,2,1,0,4,14],[6,3,4,0,0,1,16],[4,5,6,6,2,4,26],[1,1,4,3,4,3,15],[4,2,5,4,4,5,15],[4,0,0,2,3,5,13],[2,4,6,4,3,5,7],[3,3,4,2,2,6,21],[0,3,0,2,3,3,15],[0,2,4,2,2,5,24],[4,1,5,4,5,4,25],[6,0,5,0,1,1,14],[4,0,5,2,1,5,8],[4,1,4,4,3,1,10],[4,4,2,1,5,0,14],[2,4,4,1,3,1,16],[4,2,3,1,2,1,26],[2,4,1,6,5,3,2],[0,2,0,4,0,0,19],[3,1,6,3,3,1,23],[6,2,3,2,4,4,16],[5,3,5,5,0,4,5],[5,0,4,3,0,2,20],[5,3,1,2,2,5,8],[3,0,6,1,0,2,10],[5,6,6,1,0,4,12],[0,6,6,4,6,4,21],[0,4,6,5,0,0,22],[0,4,2,4,4,6,16],[4,2,1,0,6,5,14],[0,1,3,5,0,3,8],[5,5,3,3,2,0,4],[1,0,3,6,2,3,18],[4,2,6,2,2,5,2],[0,2,5,5,3,6,12],[1,0,6,6,5,0,10],[6,0,0,5,5,1,24],[1,4,6,5,6,3,19],[2,2,4,2,4,2,20],[5,6,1,4,0,5,3],[3,3,2,2,1,0,14],[0,1,3,6,5,0,9],[5,3,6,5,3,3,11],[5,3,3,1,0,2,26],[0,1,1,4,2,1,16],[4,2,3,2,1,4,6],[0,2,1,3,3,5,15],[5,6,4,1,2,5,18],[1,0,0,1,6,1,16],[2,0,6,6,2,2,17],[4,4,0,2,4,6,12],[0,5,2,5,4,6,6],[5,2,1,6,2,1,24],[2,0,2,2,0,1,14],[1,1,0,5,3,5,16],[0,2,3,5,5,5,6],[3,2,0,6,4,6,8],[4,0,1,4,5,1,6],[5,0,5,6,6,3,7],[2,6,0,0,2,1,25],[0,4,6,1,4,4,6],[6,3,1,4,1,1,24],[6,2,1,2,1,4,4],[0,1,2,3,0,1,3],[0,2,5,6,5,2,13],[2,6,4,2,2,3,17],[3,4,5,0,5,4,20],[6,2,3,4,1,3,4],[6,4,0,0,0,5,16],[3,1,2,5,0,6,11],[1,3,2,2,5,6,14],[1,3,4,5,3,5,18],[2,1,1,2,6,1,1],[4,0,4,0,6,6,8],[4,6,0,5,0,2,1],[3,1,0,5,3,2,26],[4,0,4,0,6,6,6],[5,0,0,0,0,4,26],[4,3,2,2,0,2,14],[5,2,4,0,2,2,26],[3,4,6,0,2,4,25],[2,1,5,5,1,3,26],[0,5,2,4,0,2,24],[5,2,5,4,5,0,1],[5,3,0,1,5,4,15],[6,1,5,1,2,1,21],[2,5,1,2,1,4,15],[1,4,4,0,0,0,1],[5,0,6,1,1,4,22],[0,1,1,6,1,4,1],[1,6,0,3,2,2,17],[3,4,3,3,1,5,17],[1,5,5,4,5,2,27],[0,6,5,5,0,0,26],[1,4,0,3,1,0,13],[1,0,3,5,2,4,5],[2,2,2,3,0,0,11],[3,2,2,1,1,1,6],[6,6,1,1,1,6,26],[1,5,1,2,5,2,12]]
needs   = [6,6,6,1,6,6]
print(s.shoppingOffers(price, special, needs))