class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.ans = []
        self.cnt = collections.defaultdict(int)
        self.mode = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        _sum = left + right + root.val
        self.cnt[_sum] += 1
        if self.cnt[_sum] > self.mode:
            self.mode = self.cnt[_sum]
            self.ans = [_sum]
        elif self.cnt[_sum] == self.mode:
            self.ans.append(_sum)
        return _sum
