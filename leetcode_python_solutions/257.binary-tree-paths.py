#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        self.ans = []
        self.dfs(root, [])
        return self.ans
    
    def dfs(self, root, path):
        if not root: return
        path.append(root.val)
        if not root.left and not root.right:
            self.ans.append('->'.join(map(str, path[:])))
        else:
            self.dfs(root.left, path)
            self.dfs(root.right, path)
        path.pop()

# @lc code=end

