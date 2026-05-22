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
            j = i
            while j + 1 < len(candidates) and candidates[j] == candidates[j + 1]:
                j += 1
            dfs(j + 1, seq, diff)
            seq.append(candidates[i])
            dfs(i + 1, seq, diff - candidates[i])
            seq.pop()
        dfs(0, [], target)
        return sums