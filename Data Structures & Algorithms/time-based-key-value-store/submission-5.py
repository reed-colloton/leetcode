class TimeMap:

    def __init__(self):
        self.mp = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        times = self.mp[key]
        if not times:
            return ''
        l, r = 0, len(times) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if timestamp >= times[mid][1]:
                l = mid + 1
            else:
                r = mid - 1
        return times[r][0] if r >= 0 else ''
        
