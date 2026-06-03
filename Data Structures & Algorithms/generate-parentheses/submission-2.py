class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strs = []
        s = []
        def dfs(opened, closed):
            if closed == n:
                strs.append(''.join(s))
                return
            if opened > closed:
                s.append(')')
                dfs(opened, closed + 1)
                s.pop()
            if opened < n:
                s.append('(')
                dfs(opened + 1, closed)
                s.pop()
        dfs(0, 0)
        return strs