class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = -1
        for i in range(len(prices) - 1):
            profit = max(prices[i + 1:]) - prices[i]
            if profit > highest_profit:
                highest_profit = profit
        if highest_profit == -1:
            return 0
        return highest_profit