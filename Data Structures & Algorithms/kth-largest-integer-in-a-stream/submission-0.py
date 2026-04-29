class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        while len(self.heap) > k:
            self.heap.remove(min(self.heap))

    def add(self, val: int) -> int:
        self.heap.append(val)
        while len(self.heap) > self.k:
            self.heap.remove(min(self.heap))
        return min(self.heap)
