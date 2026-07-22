class Solution:
    def rob(self, nums: List[int]) -> int:
        adjacent = far = 0
        for i in range(len(nums)):
            adjacent, far = max(adjacent, nums[i] + far), adjacent
        return adjacent
