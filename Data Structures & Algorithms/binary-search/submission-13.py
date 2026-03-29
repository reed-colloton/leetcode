class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        return self.search_helper(nums, target, 0, len(nums) - 1)
    
    def search_helper(self, nums: List[int], target: int, start: int, end: int) -> int:
        print('start', start, 'end', end)
        print('mid', start + (end - start) // 2, '=', nums[start + (end - start) // 2])
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        if start == end:
            return -1
        if nums[mid] < target:
            return self.search_helper(nums, target, mid + 1, end)
        if nums[mid] > target:
            return self.search_helper(nums, target, start, mid)
