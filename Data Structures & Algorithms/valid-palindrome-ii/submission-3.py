class Solution:
    def validPalindromeHelper(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.validPalindromeHelper(s[:i] + s[i + 1:]) \
                    or self.validPalindromeHelper(s[:j] + s[j + 1:])
            i += 1
            j -= 1
        return True


    def naiveValidPalindrome(self, s: str) -> bool:
        has_skipped = False
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if has_skipped:
                    return False
                if s[i] == s[j - 1]:
                    j -= 1
                elif s[i + 1] == s[j]:
                    i += 1
                else:
                    return False
                has_skipped = True
            i += 1
            j -= 1
        return True