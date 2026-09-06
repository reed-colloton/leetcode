class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def backtrack(i, xor):
            if i == len(nums):
                return xor
            return (
                backtrack(i + 1, xor ^ nums[i])
                + backtrack(i + 1, xor)
            )
        
        return backtrack(0, 0)
