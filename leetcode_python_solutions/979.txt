class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.cnt = 0
        self.dfs(root)
        return self.cnt
    
    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.cnt += abs(left) + abs(right)
        return root.val + left + right - 1
