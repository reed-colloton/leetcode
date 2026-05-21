class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []
        def dfs(i, seq, remainder):
            if remainder == 0:
                sums.append(seq.copy())
                return
            if i == len(nums) or remainder < 0:
                return
            dfs(i + 1, seq, remainder)
            seq.append(nums[i])
            dfs(i, seq, remainder - nums[i])
            seq.pop()
        dfs(0, [], target)
        return sums