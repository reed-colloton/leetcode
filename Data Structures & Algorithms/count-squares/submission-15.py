class CountSquares:
    def __init__(self):
        self.points = []
        self.counts = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points.append((x, y))
        self.counts[(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        for (xi, yi), diagonals in self.counts.items():
            if abs(xi - x) == abs(yi - y) and xi != x:
                # if points don't exist, will be 0
                squares += diagonals * self.counts[(x, yi)] * self.counts[(xi, y)]
        return squares
