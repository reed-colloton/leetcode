class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        counts = defaultdict(int)
        for x in hand:
            counts[x] += 1
        
        for x in hand:
            start = x
            while counts[start - 1]:
                start -= 1
            for start in range(start, start + groupSize + 1):
                while counts[start]:
                    for i in range(start, start + groupSize):
                        if counts[i] == 0:
                            return False
                        counts[i] -= 1
        return True