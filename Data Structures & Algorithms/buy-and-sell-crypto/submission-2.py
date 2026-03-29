class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = -1
        for i in range(len(prices) - 1):
            profit = max(prices[i + 1:]) - prices[i]
            highest_profit = max(profit, highest_profit)
        return max(highest_profit, 0)