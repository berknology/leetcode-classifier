#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        num_list = [(i, num) for i, num in enumerate(nums)]
        self.res = [0]*len(nums)
        self.merge_sort(num_list)
        return self.res
    
    def merge_sort(self, num_list):
        if len(num_list) <= 1:
            return num_list
        mid = len(num_list)//2
        left = self.merge_sort(num_list[:mid])
        right = self.merge_sort(num_list[mid:])
        return self.merge(left, right)

    def merge(self, nums1, nums2):
        if not nums1 or not nums2:
            return nums1 or nums2
        i = j = 0
        ans = []
        while i < len(nums1) or j < len(nums2):
            if j == len(nums2) or (i < len(nums1) and nums1[i][-1] <= nums2[j][-1]):
                ans.append(nums1[i])
                self.res[nums1[i][0]] += j
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        return ans

# @lc code=end

