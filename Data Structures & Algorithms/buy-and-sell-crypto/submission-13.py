class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = prices[0]
        profit = 0
        for p in prices:
            bestbuy = min(bestbuy, p)
            profit = max(profit, p - bestbuy)
        return profit