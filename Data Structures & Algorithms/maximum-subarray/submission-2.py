class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        current = float('-inf')
        for num in nums:
            current = max(num, current + num)
            best = max(best, current)
        return best