class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def dfs(i, l):
            if i > n:
                if len(l) == k:
                    combinations.append(l.copy())
                return
            l.append(i)
            dfs(i + 1, l)
            l.pop()
            dfs(i + 1, l)
        dfs(1, [])
        return combinations