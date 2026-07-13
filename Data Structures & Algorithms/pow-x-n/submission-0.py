class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 1:
            for _ in range(-n):
                res /= x
                print(res)
        else:
            for _ in range(n):
                res *= x
                print(res)
        return res