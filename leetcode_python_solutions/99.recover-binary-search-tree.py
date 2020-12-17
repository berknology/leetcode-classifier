#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.node1 = None
        self.node2 = None
        self.pre = None
        self.dfs(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
    
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.pre:
            if self.pre.val > root.val:
                if not self.node1:
                    self.node1 = self.pre
                self.node2 = root
        self.pre = root
        self.dfs(root.right)

# [1,5,3,4,2]

# @lc code=end

