class Solution:
    def numDecodings(self, s: str) -> int:
        memos = {}

        def dfs(i):
            if i == len(s):
                return 1
            c1 = s[i]
            if i in memos:
                return memos[i]
            if c1 == '0':
                return 0
            paths = dfs(i + 1)
            if i + 1 < len(s) and (c1 == '1' or c1 == '2' and ord(s[i + 1]) <= ord('6')):
                paths += dfs(i + 2)
            memos[i] = paths
            return paths

        return dfs(0)
