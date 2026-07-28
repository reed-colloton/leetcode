class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_min = 1 
        cur_max = 1
        res = float('-inf')

        for num in nums:
            prev_max = num * cur_max
            prev_min = num * cur_min
            cur_max = max(num, prev_max, prev_min)
            cur_min = min(num, prev_max, prev_min)
            res = max(res, cur_max)

        return res