class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []
        def dfs(nums, i, seq):
            if sum(seq) > target:
                return
            if sum(seq) == target:
                sums.append(list(seq))
                return
            if i == len(nums):
                return
            dfs(nums, i + 1, seq)
            seq.append(nums[i])
            dfs(nums, i, seq)
            seq.pop()
        dfs(nums, 0, [])
        return sums