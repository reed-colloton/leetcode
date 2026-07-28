class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_min = 1 
        cur_max = 1
        res = float('-inf')

        for num in nums:
            tmp = cur_max * num
            cur_max = max(num, cur_max * num, num * cur_min)
            cur_min = min(num, num * cur_min, tmp)
            res = max(res, cur_max)

        return res