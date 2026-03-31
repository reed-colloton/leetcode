class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        times = self.store[key]
        result = ''
        l, r = 0, len(times) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if times[mid][0] <= timestamp:
                result = times[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return result
        
