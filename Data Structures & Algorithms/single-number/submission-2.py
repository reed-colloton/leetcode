class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = set()
        for num in nums:
            print(hash_table)
            if num in hash_table:
                print('out', num)
                hash_table.remove(num)
            else:
                print('in', num)
                hash_table.add(num)
        return hash_table.pop()
            