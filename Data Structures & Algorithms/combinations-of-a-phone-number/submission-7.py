class Solution:
    to_letter = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl',
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz',
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        buffer = []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(buffer))
                return
            for char in self.to_letter[digits[i]]:
                buffer.append(char)
                dfs(i + 1)
                buffer.pop()
        dfs(0)
        return res
