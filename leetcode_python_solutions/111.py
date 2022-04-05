class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: 
            return 1 + self.minDepth(root.right)
        elif not root.right: 
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
