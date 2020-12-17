#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: 
            return False
        return self.is_same_tree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same_tree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            if s.val != t.val:
                return False
            else:
                return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)

# @lc code=end

