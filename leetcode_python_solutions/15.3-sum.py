#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2: return []
        nums.sort()
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i+1, n-1
            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                if summation == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                elif summation < 0:
                    left += 1
                else:
                    right -= 1
        return ans
# @lc code=end

