class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right-left)//2
            if self.cal_num(nums, mid) < k:
                left = mid +1 
            else:
                right = mid
        return left
    
    def cal_num(self, nums, mid):
        ans = 0
        p1 = 0
        p2 = 1
        while p2 < len(nums):
            while nums[p2] - nums[p1] > mid:
                p1 += 1
            ans += p2 - p1
            p2 += 1
        return ans
        
        
"""
Naive solution
get all the pairs O(N^2) and sort N^2long(N^2)

Binary search



3-th smallest
[1, 2, 2, 5, 6, 6]
    p1       p2





"""
