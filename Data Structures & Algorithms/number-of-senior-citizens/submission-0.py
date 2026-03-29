class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = [int(detail[-4:-2]) for detail in details]
        num_elderly = len([age for age in ages if age > 60])
        return num_elderly