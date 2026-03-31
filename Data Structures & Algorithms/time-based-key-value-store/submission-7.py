class TimeMap:

    def __init__(self):
        self.mp = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.mp[key]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if timestamp >= self.mp[key][mid][1]:
                l = mid + 1
            else:
                r = mid - 1
        return self.mp[key][r][0] if r >= 0 else ''
        
