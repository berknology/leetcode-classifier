# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        n_left = n_right = 0
        if root.left and root.left.val == root.val:
            n_left = left + 1
        if root.right and root.right.val == root.val:
            n_right = right + 1
        self.ans = max(self.ans, n_left+n_right)
        return max(n_left, n_right)

