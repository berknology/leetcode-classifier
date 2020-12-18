class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        self.dfs(root)
        return self.ans-1
    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(self.ans, 1+left+right)
        return 1+max(left, right)
