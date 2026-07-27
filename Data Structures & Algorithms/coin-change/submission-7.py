class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memos: dict[int, int] = {}

        def dfs(diff):
            if diff == 0:
                return 0

            if diff < 0:
                return float('inf')

            if diff in memos:
                return memos[diff]

            result = float('inf')
            for coin in coins:
                result = min(result, 1 + dfs(diff - coin))

            memos[diff] = result
            return result
        
        n = dfs(amount)
        if n == float('inf'):
            return -1
        return n 
