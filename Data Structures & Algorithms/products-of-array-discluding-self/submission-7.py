import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        product = math.prod([x for x in nums if x != 0])
        if zero_count == 1:
            return [product if x == 0 else 0 for x in nums]
        else:
            return [product // x for x in nums]