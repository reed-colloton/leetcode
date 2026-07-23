class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        adjacent = far = 0

        for i in range(len(nums) - 1):
            adjacent, far = max(adjacent, nums[i] + far), adjacent

        normal = adjacent
        adjacent = far = 0

        for i in range(1, len(nums)):
            adjacent, far = max(adjacent, nums[i] + far), adjacent

        return max(normal, adjacent)
