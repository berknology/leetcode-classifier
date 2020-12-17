#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        preorder.reverse()
        root = self.build_bst(preorder, float('-inf'), float('inf'))
        return root
    
    def build_bst(self, preorder, _min, _max):
        if preorder and _min < preorder[-1] < _max:
            root = TreeNode(preorder.pop())
            root.left = self.build_bst(preorder, _min, root.val)
            root.right = self.build_bst(preorder, root.val, _max)
            return root

# @lc code=end

