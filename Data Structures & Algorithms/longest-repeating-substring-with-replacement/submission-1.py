class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        highest_count = 0
        longest_len = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            highest_count = max(highest_count, counts[s[r]])
            if r - l + 1 - highest_count > k:
                counts[s[l]] -= 1
                l += 1
            longest_len = max(longest_len, r - l + 1)
        return longest_len
            
            