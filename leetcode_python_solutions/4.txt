class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (m+n+1)//2
        left, right = 0, m
        while left < right:
            mid = left + (right-left)//2
            if nums1[mid] < nums2[k - mid-1]:
                left = mid + 1
            else:
                right = mid
        
        n1 = left
        n2 = k - left
        if n1 == 0:
            mid1 = nums2[n2-1]
        elif n2 == 0:
            mid1 = nums1[n1-1]
        else:
            mid1 = max(nums1[n1-1], nums2[n2-1])
        
        if (m+n)%2 != 0:
            return mid1

        if n1 == m:
            mid2 = nums2[n2]
        elif n2 == n:
            mid2 = nums1[n1]
        else:
            mid2 = min(nums1[n1], nums2[n2])
        return (mid1+mid2)/2


"""

   m1 n1
2, 4, 9
1, 3, 7, 8
   m2 n2


1, 2, 3,   4,     7,   8, 9
         mid1    mid2

m = 3
n = 4
k = (m+n)//2 = 3


"""
