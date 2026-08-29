class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda t: t[1])
        removals = 0
        previous_end = float('-inf')
        for interval in intervals:
            if interval[0] < previous_end:
                removals += 1
            else:
                previous_end = interval[1]
        return removals
            
