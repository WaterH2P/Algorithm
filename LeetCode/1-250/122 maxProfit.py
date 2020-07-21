# 【简单】122. 买卖股票的最佳时机 II
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1: return 0
        profit = 0
        minPrice = maxPrice = prices.pop(0)
        for price in prices:
            if price > maxPrice: maxPrice = price
            if price < maxPrice:
                profit += maxPrice - minPrice
                minPrice = maxPrice = price
        return profit + maxPrice - minPrice


if __name__ == '__main__':
    s = Solution()

    result = 7
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))

    result = 4
    prices = [1,2,3,4,5]
    print(s.maxProfit(prices))