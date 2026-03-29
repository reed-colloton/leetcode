class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for price in prices:
            profit = max(price - lowest, profit)
            lowest = min(price, lowest)
        return profit