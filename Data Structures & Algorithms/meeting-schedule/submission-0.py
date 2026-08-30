"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda t: t.start)
        previous_end = float('-inf')
        for interval in intervals:
            if interval.start < previous_end:
                return False
            previous_end = interval.end
        return True
            
