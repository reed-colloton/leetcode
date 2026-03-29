class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq, window_freq = {}, {}
        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)
        shortest = ''
        l = 0
        for r in range(len(s)):
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1
            while all([True if window_freq.get(num, 0) - t_freq[num] >= 0 else False for num in t_freq.keys()]):
                if not shortest or r - l + 1 < len(shortest):
                    shortest = s[l: r + 1]
                window_freq[s[l]] -= 1
                l += 1
        return shortest