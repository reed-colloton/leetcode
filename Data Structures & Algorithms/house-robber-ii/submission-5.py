class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(start, end):
            adjacent = far = 0
            for i in range(start, end):
                adjacent, far = max(adjacent, nums[i] + far), adjacent
            return adjacent

        return max(nums[0], helper(0, len(nums) - 1), helper(1, len(nums)))
