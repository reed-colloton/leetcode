class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starts = []
        for num in nums:
            if num - 1 not in nums_set:
                starts.append(num)
        longest = 0
        for start in starts:
            length = 1
            while start + length in nums_set:
                length += 1
            longest = max(longest, length)
        return longest