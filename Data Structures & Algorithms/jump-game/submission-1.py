class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        target = i
        while i > 0:
            i -= 1
            if i + nums[i] >= target:
                target = i
        return target == 0