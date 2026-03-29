class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            counts = str(counts)
            if counts in anagrams:
                anagrams[counts].append(s)
            else:
                anagrams[counts] = [s]
        return list(anagrams.values())
