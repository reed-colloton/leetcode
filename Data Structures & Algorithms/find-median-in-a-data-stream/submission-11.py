class MedianFinder:

    def __init__(self):
        self.lesser = []
        self.greater = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lesser, -num)
        x = -heapq.heappop(self.lesser)
        heapq.heappush(self.greater, x)
        if len(self.greater) > 1 + len(self.lesser):
            x = heapq.heappop(self.greater)
            heapq.heappush(self.lesser, -x)

    def findMedian(self) -> float:
        if len(self.greater) > len(self.lesser):
            return self.greater[0]
        else:
            return 0.5 * (self.greater[0] - self.lesser[0])
