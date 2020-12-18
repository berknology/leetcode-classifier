class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        _left = max(left, 0)
        _right = max(right, 0)
        self.ans = max(self.ans, _left+_right+root.val)
        return root.val + max(_left, _right)
