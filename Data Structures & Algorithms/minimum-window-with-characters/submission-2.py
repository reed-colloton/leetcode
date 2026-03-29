class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq, window_freq = {}, {}
        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)
        shortest = ''
        have, need = 0, len(t_freq)
        l = 0
        for r in range(len(s)):
            window_freq[s[r]] = 1 + window_freq.get(s[r], 0)
            if window_freq[s[r]] == t_freq.get(s[r]):
                have += 1
            while have == need:
                if not shortest or r - l + 1 < len(shortest):
                    shortest = s[l: r + 1]
                window_freq[s[l]] -= 1
                if window_freq[s[l]] < t_freq.get(s[l], 0):
                    have -= 1
                l += 1

        return shortest