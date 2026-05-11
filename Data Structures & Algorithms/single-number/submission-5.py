class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unmatched = nums[0]
        for i in range(1, len(nums)):
            unmatched ^= nums[i]
        return unmatched