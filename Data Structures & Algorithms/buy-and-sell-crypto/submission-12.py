class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallestBuy = prices[0]
        profit = 0
        for p in prices:
            smallestBuy = min(smallestBuy, p)
            profit = max(profit, p - smallestBuy)
            print(profit)
        return profit