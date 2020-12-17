#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.traverse(root)
        return self.ans
    
    def traverse(self, root):
        if not root: return 0
        _left = 0
        if root.left:
            left = self.traverse(root.left)
            if root.val == root.left.val:
                _left += left
        _right = 0
        if root.right:
            right = self.traverse(root.right)
            if root.val == root.right.val:
                _right += right
        self.ans = max(self.ans, _left+_right)
        return 1+max(_left, _right)

# @lc code=end

