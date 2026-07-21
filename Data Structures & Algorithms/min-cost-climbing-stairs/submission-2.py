class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first = cost[0]
        second = cost[1]
        for i in range(2, n):
            second, first = min(first, second) + cost[i], second
        return min(second, first)