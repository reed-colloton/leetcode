class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = 0
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0