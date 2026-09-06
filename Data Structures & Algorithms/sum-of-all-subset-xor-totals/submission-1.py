class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        total = 0

        def backtrack(i, xor):
            if i == len(nums):
                nonlocal total
                total += xor
                return
            backtrack(i + 1, xor)
            backtrack(i + 1, xor ^ nums[i])
        
        backtrack(0, 0)
        return total
