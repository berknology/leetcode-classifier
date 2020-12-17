#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            k -= 1
            if k == 0: return node.val
            current = node.right

# @lc code=end

