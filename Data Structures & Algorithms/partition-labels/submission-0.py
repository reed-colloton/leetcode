class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        furthest = {}
        for i in range(len(s)):
            furthest[s[i]] = i
        substrings = []
        end = 0
        size = 0
        for i in range(len(s)):
            size += 1
            end = max(end, furthest[s[i]])
            if i == end:
                substrings += [size]
                size = 0
        return substrings