# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        covered = {None}
        self.dfs(root, covered, None)
        return self.ans
    
    def dfs(self, root, covered, par):
        if not root:
            return
        self.dfs(root.left, covered, root)
        self.dfs(root.right, covered, root)
        if (root.left not in covered or root.right not in covered) or (not par and root not in covered):
            self.ans += 1
            covered.add(root.left)
            covered.add(root.right)
            covered.add(root)
            covered.add(par)
