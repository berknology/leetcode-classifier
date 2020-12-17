#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = []
        self.find_leaves(root1, l1)
        l2 = []
        self.find_leaves(root2, l2)
        return l1 == l2

    def find_leaves(self, root, leaves):
        if not root: return
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        self.find_leaves(root.left, leaves)
        self.find_leaves(root.right, leaves)

# @lc code=end

