class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            new = 0
            for x in str(n):
                new += int(x) ** 2
            n = new
        return True