#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = float('inf')
        self.pre = None
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.pre:
            self.ans = min(self.ans, abs(root.val-self.pre.val))
        self.pre = root
        self.dfs(root.right)
    
# @lc code=end

