class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            change[bill] += 1
            while bill > 10 and change[10]:
                bill -= 10
                change[10] -= 1
            while bill > 5 and change[5]:
                bill -= 5
                change[5] -= 1
            if bill != 5:
                return False
        print(change)
        return True


