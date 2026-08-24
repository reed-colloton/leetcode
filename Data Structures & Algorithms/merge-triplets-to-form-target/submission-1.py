class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        one = two = three = False
        for x, y, z in triplets:
            if not one and x == target[0]:
                if y <= target[1] and z <= target[2]:
                    one = True
            if not two and y == target[1]:
                if x <= target[0] and z <= target[2]:
                    two = True
            if not three and z == target[2]:
                if x <= target[0] and y <= target[1]:
                    three = True
            if all([one, two, three]):
                return True
        return False