class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged_word = ''
        while i < len(word1) and i < len(word2):
            merged_word += word1[i]
            merged_word += word2[i]
            i += 1
        return merged_word + word1[i:] + word2[i:]