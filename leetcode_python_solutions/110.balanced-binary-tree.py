#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.is_balanced = True
        self.find_height(root)
        return self.is_balanced

    def find_height(self, root):
        if not root: return 0
        left_height = self.find_height(root.left)
        right_height = self.find_height(root.right)
        if abs(left_height - right_height) > 1:
            self.is_balanced = False
        return 1 + max(left_height, right_height)


# @lc code=end

