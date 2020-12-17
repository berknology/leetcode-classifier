#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        if not left and not right and root.val == 0:
            return None
        else:
            root.left = left
            root.right = right
            return root
        
# @lc code=end

