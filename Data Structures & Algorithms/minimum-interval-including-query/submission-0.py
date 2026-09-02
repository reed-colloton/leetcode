class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        output = {}
        i = 0
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            output[query] = min_heap[0][0] if min_heap else -1
        return [output[query] for query in queries]

