import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod([x for x in nums if x != 0])
        zero_count = nums.count(0)
        if zero_count == 0:
            return [int(product / x) for x in nums]
        if zero_count == 1:
            return [product if x == 0 else 0 for x in nums]
        else:
            return [0] * len(nums)