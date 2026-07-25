class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand(start, end):
            substrings = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                substrings += 1
                start -= 1
                end += 1
            return substrings

        res = 0
        for mid in range(len(s)):
            res += expand(mid, mid)
            res += expand(mid, mid + 1)
        
        return res
            