class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        indices = set()

        def expand(start, end):
            while start >= 0 and end < n and s[start] == s[end]:
                indices.add((start, end))
                start -= 1
                end += 1
            return start + 1, end - 1
        
        for mid in range(n):
            odd = expand(mid, mid)
            even = expand(mid, mid + 1)
        
        return len(indices)
            