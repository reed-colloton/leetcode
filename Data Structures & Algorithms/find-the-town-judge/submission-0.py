class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {i: [] for i in range(1, n + 1)}
        trusted = {i: [] for i in range(1, n + 1)}
        for a, b in trust:
            trusts[a].append(b)
            trusted[b].append(a)
        for i in range(1, n + 1):
            if len(trusted[i]) == n - 1 and len(trusts[i]) == 0:
                return i
        return -1
        