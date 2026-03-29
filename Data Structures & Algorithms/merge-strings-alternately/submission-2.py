class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = '' 
        n, m = len(word1), len(word2)       
        i = 0
        while i < min(n, m):
            merged += word1[i]
            merged += word2[i]
            i += 1
        return merged + word1[i:] + word2[i:]