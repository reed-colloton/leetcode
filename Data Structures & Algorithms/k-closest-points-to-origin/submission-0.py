class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for x, y in points:
            d = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(distances, (-d, [x, y]))
            if len(distances) > k:
                heapq.heappop(distances)
        return [p for d, p in distances]
