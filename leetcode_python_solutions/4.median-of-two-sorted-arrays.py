#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        k = (m+n+1)//2
        left, right = 0, m
        while left < right:
            mid1 = left + (right-left)//2
            mid2 = k - mid1
            if nums1[mid1] < nums2[mid2-1]:
                left = mid1 + 1
            else:
                right = mid1
             
        mid1 = left
        mid2 = k - left
        
        if mid1 == 0:
            c1 = nums2[mid2-1]
        elif mid2 == 0:
            c1 = nums1[mid1-1]
        else:
            c1 = max(nums1[mid1-1], nums2[mid2-1])
        
        if (m+n+1)%2 == 0:
            return c1
        else:
            if mid1 == m:
                c2 = nums2[mid2]
            elif mid2 == n:
                c2 = nums1[mid1]
            else:
                c2 = min(nums1[mid1], nums2[mid2])
            return (c1+c2)/2
        

# @lc code=end

