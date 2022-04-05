class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if root.left and not root.left.left and not root.left.right:
            self.ans += root.left.val
        self.dfs(root.right)
