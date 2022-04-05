class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
    def dfs(self, root, cum_sum):
        if not root: return
        cum_sum = cum_sum*10 + root.val
        if not root.left and not root.right:
            self.ans += cum_sum
        else:
            self.dfs(root.left, cum_sum)
            self.dfs(root.right, cum_sum)
    
