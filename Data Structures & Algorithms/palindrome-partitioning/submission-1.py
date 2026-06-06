class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, j, partitions):
            if i == len(s):
                res.append(partitions)
                return
            if j > len(s):
                return
            if s[i:j] == s[i:j][::-1]:
                dfs(j, j + 1, partitions + [s[i:j]])
            dfs(i, j + 1, partitions)
        dfs(0, 1, [])
        return res
