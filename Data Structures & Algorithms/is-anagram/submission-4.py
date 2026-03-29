class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = list(s)
        for c in t:
            if c in s_chars:
                s_chars.remove(c)
            else:
                return False
        t_chars = list(t)
        for c in s:
            if c in t_chars:
                t_chars.remove(c)
            else:
                return False
        return True