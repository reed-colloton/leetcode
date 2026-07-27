class Solution:
    def numDecodings(self, s: str) -> int:
        memos = {}

        def dfs(i):
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            if i in memos:
                return memos[i]

            paths = dfs(i + 1)
            if i + 1 < len(s):
                if (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):
                    paths += dfs(i + 2)
                    
            memos[i] = paths
            return paths

        return dfs(0)
