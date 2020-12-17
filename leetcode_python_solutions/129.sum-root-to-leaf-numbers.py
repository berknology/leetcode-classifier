#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, cum_sum):
        if not root: return
        cum_sum = cum_sum*10 + root.val
        if not root.left and not root.right:
            self.ans += cum_sum
        else:
            self.dfs(root.left, cum_sum)
            self.dfs(root.right, cum_sum)
    
# @lc code=end

