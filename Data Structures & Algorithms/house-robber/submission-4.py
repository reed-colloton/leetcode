class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        adjacent = far = 0
        for i in range(n):
            tmp = adjacent
            adjacent = max(adjacent, nums[i] + far)
            far = tmp

        return max(adjacent, far)
