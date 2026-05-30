class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def bfs(i, acc):
            if i == len(nums):
                permutations.append(acc)
                return
            for j in range(len(acc) + 1):
                bfs(i + 1, acc[:j] + [nums[i]] + acc[j:])
        bfs(1, [nums[0]])
        return permutations