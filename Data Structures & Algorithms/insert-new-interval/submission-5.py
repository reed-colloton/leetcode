class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]


        overlapping = newInterval[:]
        
        for i in range(len(intervals)):
            if newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:
                overlapping[0] = min(overlapping[0], intervals[i][0])
            if newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]:
                overlapping[1] = max(overlapping[1], intervals[i][1])
        result = []
        placed = False
        for i in range(len(intervals)):
            if not placed and overlapping[0] <= intervals[i][1]:
                result.append(overlapping)
                placed = True
            if intervals[i][1] < overlapping[0] or intervals[i][0] > overlapping[1]:
                result.append(intervals[i])
        
        if not placed:
            result.append(overlapping)
        return result
            

