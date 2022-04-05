class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        if not left and not right and root.val == 0:
            return None
        else:
            root.left = left
            root.right = right
            return root
        
