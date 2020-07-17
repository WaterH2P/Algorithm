class Solution:
    def maxProfit(self, prices) -> int:
        if prices == None or len(prices) <= 1:
            return 0
        if prices[1] < prices[0]:
            prices[0] = prices[1]
        prices[1] -= prices[0]
        for i in range(2, len(prices)):
            if prices[i] < prices[0]:
                prices[0] = prices[i]
                continue
            if prices[i] - prices[0] > prices[1]:
                prices[1] = prices[i] - prices[0]
        return prices[1]

if __name__ == '__main__':
    s = Solution()
    prices = [1]
    print( s.maxProfit(prices) )