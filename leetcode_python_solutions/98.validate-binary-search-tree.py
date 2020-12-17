#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst(root, float('-inf'), float('inf'))

    def is_valid_bst(self, root, _min, _max):
        if not root: return True
        if root.val <= _min or root.val >= _max:
            return False
        return self.is_valid_bst(root.left, _min, root.val) and self.is_valid_bst(root.right, root.val, _max)

# @lc code=end

