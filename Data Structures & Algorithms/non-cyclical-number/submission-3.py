class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            new = 0
            while n:
                x = n % 10
                n //= 10
                new += x ** 2
            n = new
        return True