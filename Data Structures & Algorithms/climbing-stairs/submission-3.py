class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2
        for i in range(2, n):
            new = first + second
            first = second
            second = new
        return new

    def climbStairsFull(self, n: int) -> int:
        if n <= 2:
            return n
        paths = [0] * n
        paths[0] = 1
        paths[1] = 2
        for i in range(2, n):
            paths[i] = paths[i - 1] + paths[i - 2]
        return paths[n - 1]