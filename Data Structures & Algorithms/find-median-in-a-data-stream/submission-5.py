class MedianFinder:

    def __init__(self):
        self.lesser = []
        self.greater = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lesser, -num)
        top = heapq.heappop(self.lesser)
        heapq.heappush(self.greater, -top)
        if len(self.lesser) > 1 + len(self.greater):
            top = heapq.heappop(self.lesser)
            heapq.heappush(self.greater, -top)
        elif len(self.greater) > 1 + len(self.lesser):
            top = heapq.heappop(self.greater)
            heapq.heappush(self.lesser, -top)

    def findMedian(self) -> float:
        if len(self.lesser) > len(self.greater):
            return -self.lesser[0]
        elif len(self.greater) > len(self.lesser):
            return self.greater[0]
        else:
            return 0.5 * (self.greater[0] - self.lesser[0])
        

        