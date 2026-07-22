class Solution:
    def rob(self, nums: List[int]) -> int:
        previous = adjacent = 0
        for money in nums:
            adjacent, previous = max(adjacent, money + previous), adjacent
        return adjacent
