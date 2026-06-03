class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strs = []
        def dfs(s, opened, closed):
            if closed == n:
                strs.append(s)
                return
            if opened > closed:
                dfs(s + ')', opened, closed + 1)
            if opened < n:
                dfs(s + '(', opened + 1, closed)
        dfs('', 0, 0)
        return strs