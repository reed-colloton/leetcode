class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(' ')
        lst = [s for s in lst if s != '']
        print(lst)
        return len(lst[-1])