class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = collections.deque()
        for i in range(k-1):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        for i in range(k-1, len(nums)):
            if queue and queue[0] < i-k+1:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            ans.append(nums[queue[0]])
        return ans
        
        
"""
monotone decreasing queue
[3,2]


ans = [3,]
"""
