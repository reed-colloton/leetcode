class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sums = []
        def dfs(i, seq, diff):
            if diff == 0:
                sums.append(seq.copy())
                return
            if diff < 0 or i == len(candidates):
                return
            seq.append(candidates[i])
            dfs(i + 1, seq, diff - candidates[i])
            seq.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, seq, diff)
        dfs(0, [], target)
        return sums