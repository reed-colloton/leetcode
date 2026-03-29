class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if self.time(piles, mid) <= h:
                r = mid
            elif self.time(piles, mid) > h:
                l = mid + 1
            else:
                break
        return l

    def time(self, piles: List[int], k: int):
        return sum([math.ceil(p / k) for p in piles])