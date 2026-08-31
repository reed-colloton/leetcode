"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((1, interval.start))
            events.append((-1, interval.end))
        events.sort(key=lambda e: (e[1], e[0]))
        rooms = 0
        max_rooms = 0
        for e in events:
            rooms += e[0]
            max_rooms = max(max_rooms, rooms)
        return max_rooms
          
