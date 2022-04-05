class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.ans = [0]*len(nums)
        _ = self.merge_sort([(element, i) for i, element in enumerate(nums)])
        return self.ans
        
    def merge_sort(self, num_list):
        n = len(num_list)
        if n <= 1:
            return num_list
        mid = n//2
        left = self.merge_sort(num_list[:mid])
        right = self.merge_sort(num_list[mid:])
        return self.merge(left, right)
    
    def merge(self, nums1, nums2):
        p1 = p2 = 0
        nums = []
        while p1 < len(nums1) or p2 < len(nums2):
            if (p2 == len(nums2)) or (p1 < len(nums1) and nums1[p1][0] <= nums2[p2][0]):
                self.ans[nums1[p1][1]] += p2
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
        return nums

        
"""

divide and conquer
use merge sort

and calculate the number of smaller elements on the right in the merge step


[5,     2,      6,      1]

[5,     2]      [6,     1]               [2,     5]      [1,     6]

[5]    [2]      [6]     [1]



"""
