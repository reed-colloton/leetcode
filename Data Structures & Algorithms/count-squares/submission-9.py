class CountSquares:
    def __init__(self):
        self.points = []
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.freq[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        for xi, yi in self.points:
            if abs(xi - x) == abs(yi - y) and xi != x and yi != y:
                # if points don't exist, will be 0
                squares += self.freq[(x, yi)] * self.freq[(xi, y)]
        return squares
