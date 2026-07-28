class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_min = 1 
        cur_max = 1
        result = float('-inf')

        for num in nums:
            extend_max = num * cur_max
            extend_min = num * cur_min
            cur_max = max(num, extend_max, extend_min)
            cur_min = min(num, extend_max, extend_min)
            result = max(result, cur_max)

        return result