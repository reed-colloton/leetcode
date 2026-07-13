class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for _ in range(abs(n)):
            res *= x
            print(res)
        if n < 1:
            res = 1 / res
        return res