class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = -1
        for i in range(len(prices) - 1):
            profit = max(prices[i + 1:]) - prices[i]
            highest_profit = max(profit, highest_profit)
        if highest_profit == -1:
            return 0
        return highest_profit