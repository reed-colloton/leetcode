class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        total = 0
        xor = 0

        def backtrack(i):
            nonlocal xor
            if i == len(nums):
                nonlocal total
                total += xor
                return
            previous = xor
            backtrack(i + 1)
            xor = previous ^ nums[i]
            backtrack(i + 1)
        
        backtrack(0)
        return total
