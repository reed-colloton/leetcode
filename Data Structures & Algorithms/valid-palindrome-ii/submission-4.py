class Solution:
    def validPalindromeHelper(self, s: str, l, r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.validPalindromeHelper(s, l + 1, r) \
                    or self.validPalindromeHelper(s, l, r - 1)
            l += 1
            r -= 1
        return True
