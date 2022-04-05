class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.ans = []
        self.mode = 0
        self.cur_time = 1
        self.pre = None
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.pre == root.val:
            self.cur_time += 1
        else:
            self.cur_time = 1
        if self.cur_time > self.mode:
            self.mode = self.cur_time
            self.ans = [root.val]
        elif self.cur_time == self.mode:
            self.ans.append(root.val)
        self.pre = root.val
        self.dfs(root.right)
