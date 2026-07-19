class CountSquares:
    def __init__(self):
        self.ys = defaultdict(list)
        self.xs = defaultdict(list)
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xs[y].append(x)
        self.ys[x].append(y)
        self.points[(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0
        for xi in self.xs[y]:
            if xi == x:
                continue
            for yi in self.ys[x]:
                if yi == y:
                    continue
                if abs(yi - y) == abs(xi - x):
                    if xi in self.xs[yi] and yi in self.ys[xi]:
                        squares += self.points[(xi, yi)]
        return squares
