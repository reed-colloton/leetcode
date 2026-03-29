import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = math.inf
        profit = 0
        for price in prices:
            lowest = min(price, lowest)
            profit = max(price - lowest, profit)
        return profit