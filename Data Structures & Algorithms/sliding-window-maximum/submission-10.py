class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []        
        dq = collections.deque()
        popleft = dq.popleft
        append = dq.append
        pop = dq.pop
        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                pop()
            append(r)
            if r - k + 1 > dq[0]:
                popleft()
            if r >= k - 1:
                res.append(nums[dq[0]])
        return res