class Solution:
    def longestPalindrome(self, s: str) -> str:

        def grow(i, j):

            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            return i + 1, j - 1

        length = 0
        substring = (0, 0)

        for mid in range(len(s)):
            odd = grow(mid, mid)
            even = grow(mid, mid + 1)

            for i, j in (odd, even):
                if j - i + 1 > length:
                    length = j - i + 1
                    substring = (i, j)

        i, j = substring
        return s[i: j + 1]