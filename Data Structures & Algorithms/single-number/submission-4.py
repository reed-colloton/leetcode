class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = set()
        for num in nums:
            if num in hash_table:
                hash_table.remove(num)
            else:
                hash_table.add(num)
        return hash_table.pop()