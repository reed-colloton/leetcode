class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dynamic = [0] * n
        dynamic[0] = cost[0]
        dynamic[1] = cost[1]
        for i in range(2, n):
            dynamic[i] = min(dynamic[i - 1], dynamic[i - 2]) + cost[i]
            print(dynamic)
        return min(dynamic[n - 1], dynamic[n - 2])