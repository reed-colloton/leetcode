import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            return [product if x == 0 else 0 for x in nums]
        else:
            return [product // x for x in nums]