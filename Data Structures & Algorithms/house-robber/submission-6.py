class Solution:
    def rob(self, nums: List[int]) -> int:
        adjacent = 0
        far_enough = 0
        for loot in nums:
            adjacent, far_enough = max(adjacent, loot + far_enough), adjacent
        return adjacent
