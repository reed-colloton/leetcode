class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, mph) for pos, mph in zip(position, speed)]
        cars = sorted(cars, key=lambda pair: pair[0])
        fleets = 1
        while len(cars) >= 2:
            if (target - cars[-2][0]) / cars[-2][1] <= (target - cars[-1][0]) / cars[-1][1]:
                cars.pop(-2)
            else:
                cars.pop()
                fleets += 1
                
        return fleets
