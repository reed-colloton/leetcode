class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for x in range(n + 1):
            counts.append(self.hammingWeight(x))
        return counts

    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (1 << i) & n:
                count += 1
        return count