class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack(n, n_left=0, n_right=0, path=[])
        return self.ans
    def backtrack(self, n, n_left, n_right, path):
        if n_left == n and n_right == n:
            self.ans.append("".join(path))
        if n_left < n:
            self.backtrack(n, n_left+1, n_right, path+['('])
        if n_right < n_left:
            self.backtrack(n, n_left, n_right+1, path+[')'])
