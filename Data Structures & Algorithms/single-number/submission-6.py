class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unmatched = 0
        for num in nums:
            unmatched ^= num
        return unmatched