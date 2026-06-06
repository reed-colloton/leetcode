class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, j, partitions):
            if i == len(s):
                for sub in partitions:
                    if not sub == sub[::-1]:
                        return
                res.append(partitions)
                return
            if j > len(s):
                return
            dfs(j, j + 1, partitions + [s[i:j]])
            dfs(i, j + 1, partitions)
        dfs(0, 1, [])
        return res
