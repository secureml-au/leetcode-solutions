from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque() # stores indices, values decreasing
        res = []
        
        for i in range(len(nums)):
            # 1. Remove indices out of window
            while q and q[0] < i - k + 1:
                q.popleft()
            
            # 2. Remove smaller values from back
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            
            # 3. Add max to result once window is full
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res