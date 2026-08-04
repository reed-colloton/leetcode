class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        i = target
        while i > 0:
            i -= 1
            if i + nums[i] >= target:
                target = i
        return target == 0