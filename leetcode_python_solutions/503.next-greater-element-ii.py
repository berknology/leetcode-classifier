#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)
        ans = [-1]*n
        stack = []
        for i in range(2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                idx = stack.pop()
                ans[idx] = nums[i%n]
            stack.append(i%n)
        return ans

# @lc code=end

