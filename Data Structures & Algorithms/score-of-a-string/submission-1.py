class Solution:
    def scoreOfString(self, s: str) -> int:
        acc = 0
        for i in range(1, len(s)):
            acc += abs(ord(s[i - 1])- ord(s[i]))
        return acc