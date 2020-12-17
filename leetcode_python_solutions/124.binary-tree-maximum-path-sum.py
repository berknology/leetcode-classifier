#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        _left = max(left, 0)
        _right = max(right, 0)
        self.ans = max(self.ans, _left+_right+root.val)
        return root.val + max(_left, _right)


# @lc code=end

