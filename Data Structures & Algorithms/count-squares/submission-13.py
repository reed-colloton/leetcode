class CountSquares:
    def __init__(self):
        self.points = []
        self.counts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points.append((x, y))
        self.counts[(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        for xi, yi in self.points:
            if abs(xi - x) == abs(yi - y) and xi != x:
                # if points don't exist, will be 0
                squares += self.counts[(x, yi)] * self.counts[(xi, y)]
        return squares
