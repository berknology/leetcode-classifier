class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.hash_set = {None}
        self.ans = 0
        self.dfs(root, None)
        return self.ans
    def dfs(self, root, par):
        if not root: return
        self.dfs(root.left, root)
        self.dfs(root.right, root)
        if (not par and root not in self.hash_set) or root.left not in self.hash_set or root.right not in self.hash_set:
            self.ans += 1
            self.hash_set.add(root)
            self.hash_set.add(par)
            self.hash_set.add(root.left)
            self.hash_set.add(root.right)
        
