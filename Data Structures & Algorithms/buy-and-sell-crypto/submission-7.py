class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for r in range(1, len(prices)):
            lowest = min(prices[r], lowest)
            profit = max(prices[r] - lowest, profit)
            print(lowest, profit)
        return profit