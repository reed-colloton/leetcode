class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(start, end):
            adjacent = far = 0
            for i in range(start, end):
                adjacent, far = max(adjacent, nums[i] + far), adjacent
            return adjacent

        return max(helper(0, n - 1), helper(1, n))
