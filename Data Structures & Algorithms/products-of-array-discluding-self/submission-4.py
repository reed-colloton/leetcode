import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod([x for x in nums if x != 0])
        if nums.count(0) > 1:
            return [0] * len(nums)
        elif 0 in nums:
            return [product if x == 0 else 0 for x in nums]
        else:
            return [int(product / x) for x in nums]