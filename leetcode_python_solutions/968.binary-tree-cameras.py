#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.hash_set = {None}
        self.ans = 0
        self.dfs(root, None)
        return self.ans

    def dfs(self, root, par):
        if not root: return
        self.dfs(root.left, root)
        self.dfs(root.right, root)
        if (not par and root not in self.hash_set) or root.left not in self.hash_set or root.right not in self.hash_set:
            self.ans += 1
            self.hash_set.add(root)
            self.hash_set.add(par)
            self.hash_set.add(root.left)
            self.hash_set.add(root.right)
        

# @lc code=end

