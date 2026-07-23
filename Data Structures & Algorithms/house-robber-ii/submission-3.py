class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        adjacent = far = 0
        for i in range(n - 1):
            adjacent, far = max(adjacent, nums[i] + far), adjacent
        consider_first = adjacent

        adjacent = far = 0
        for i in range(1, n):
            adjacent, far = max(adjacent, nums[i] + far), adjacent
        skip_first = adjacent

        return max(consider_first, skip_first)
