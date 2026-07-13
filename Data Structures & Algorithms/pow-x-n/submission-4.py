class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        exp = abs(n)
        while exp > 0:
            if exp & 1:
                res *= x
            x *= x
            exp >>= 1
        if n < 0:
            return 1 / res
        return res