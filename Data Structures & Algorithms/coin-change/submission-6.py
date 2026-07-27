class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memos: dict[tuple[int, int], int] = {}

        def dfs(i, diff):
            if diff == 0:
                return 0
            if diff < 0 or i == len(coins):
                return float('inf')
            if (i, diff) in memos:
                return memos[(i, diff)]
            skip = dfs(i + 1, diff)
            use = 1 + dfs(i, diff - coins[i])
            n = min(skip, use)
            memos[(i, diff)] = n
            return n
        
        n = dfs(0, amount)
        if n == float('inf'):
            return -1
        return n 
