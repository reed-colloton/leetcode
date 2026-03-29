class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        keep = [num for num in nums if num != val]
        for i, num in enumerate(keep):
            nums[i] = num
        return len(keep)