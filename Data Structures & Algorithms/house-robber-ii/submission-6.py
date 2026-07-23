class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(offset):
            adjacent = far = 0
            for i in range(offset, len(nums) - 1 + offset):
                adjacent, far = max(adjacent, nums[i] + far), adjacent
            return adjacent

        return max(nums[0], helper(0), helper(1))
