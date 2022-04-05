class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = float('inf')
        self.pre = None
        self.dfs(root)
        return self.ans
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.pre:
            self.ans = min(self.ans, abs(root.val-self.pre.val))
        self.pre = root
        self.dfs(root.right)
    
